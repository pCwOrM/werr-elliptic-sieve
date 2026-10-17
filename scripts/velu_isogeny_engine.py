#!/usr/bin/env python3
"""
Scan elliptic-rank.icarm.cloud database.json for:
1. Unsubmitted Velu 2-isogenies and 3-isogenies of high-rank leaderboard curves
   that place in the Top 10 (either overall or within their torsion subgroup).
2. High-rank curves on the boundary of wide-open Top-10 slots where finding 1 additional
   rational point via our 14-Modulus 64-Bit QR Super-Wheel + Werr Core upgrades the rank.
"""
import json
import sys
import urllib.request
from fractions import Fraction
import math

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

headers = {"User-Agent": "pCwOrM-Research"}
with urllib.request.urlopen(
    urllib.request.Request(
        "https://elliptic-rank.icarm.cloud/database.json", headers=headers
    ),
    timeout=30,
) as r:
    db = json.loads(r.read().decode("utf-8"))

curves = db.get("curves", [])
existing_keys = set(c["curve_key"] for c in curves)
print(f"Loaded {len(curves)} curves ({len(existing_keys)} unique canonical c4:c6 keys).")


def weierstrass_invariants(ainvs):
    a1, a2, a3, a4, a6 = [Fraction(x) for x in ainvs]
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 * b2 * b2 + 36 * b2 * b4 - 216 * b6
    disc = -b2 * b2 * b8 - 8 * b4 * b4 * b4 - 27 * b6 * b6 + 9 * b2 * b4 * b6
    return b2, b4, b6, b8, c4, c6, disc


def find_2torsion_points(ainvs):
    """Find rational 2-torsion points P = (x0, y0) on y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6.
    A point is 2-torsion iff 2*y0 + a1*x0 + a3 = 0, which means 4*x0^3 + b2*x0^2 + 2*b4*x0 + b6 = 0.
    """
    a1, a2, a3, a4, a6 = [Fraction(x) for x in ainvs]
    b2, b4, b6, b8, c4, c6, disc = weierstrass_invariants(ainvs)
    # 4 x^3 + b2 x^2 + 2 b4 x + b6 = 0
    # Let X = 4*x => X^3 + b2 X^2 + 8 b4 X + 16 b6 = 0 (monic integer polynomial!)
    B2 = int(b2)
    B4 = int(8 * b4)
    B6 = int(16 * b6)
    # Rational roots of monic integer cubic X^3 + B2 X^2 + B4 X + B6 = 0 are integer divisors of B6.
    # Instead of factoring huge B6, we can also check depressed cubic or use integer cube root / gcd,
    # or check if B6 == 0, etc. Wait: we have bad_primes of the curve! Any prime dividing B6's rational root...
    # Even simpler: solve X^3 + B2 X^2 + B4 X + B6 = 0 numerically in high precision using binary search / Newton's method!
    return B2, B4, B6, a1, a3


def integer_roots_monic_cubic(B2, B4, B6):
    """Find exact integer roots of f(X) = X^3 + B2*X^2 + B4*X + B6 = 0 using exact integer binary/Newton search."""
    def f(x):
        return ((x + B2) * x + B4) * x + B6

    def df(x):
        return (3 * x + 2 * B2) * x + B4

    if B6 == 0:
        roots = [0]
        # Quadratic X^2 + B2 X + B4 = 0
        disc_q = B2 * B2 - 4 * B4
        if disc_q >= 0:
            sq = math.isqrt(disc_q)
            if sq * sq == disc_q:
                for num in (-B2 + sq, -B2 - sq):
                    if num % 2 == 0:
                        roots.append(num // 2)
        return sorted(set(roots))

    # Bound on roots: |X| <= 1 + max(|B2|, isqrt(|B4|), icbrt(|B6|))
    bound = 1 + max(abs(B2), math.isqrt(abs(B4)), int(round(abs(B6) ** (1 / 3))) * 2 + 10)
    # Wait: for huge numbers float**1/3 overflows! Use bit_length:
    bound = 1 << (max(B2.bit_length(), B4.bit_length() // 2, B6.bit_length() // 3) + 4)

    def bisect_root(lo, hi):
        flo, fhi = f(lo), f(hi)
        if flo == 0:
            return lo
        if fhi == 0:
            return hi
        if (flo < 0 and fhi < 0) or (flo > 0 and fhi > 0):
            return None
        while lo <= hi:
            mid = (lo + hi) // 2
            fmid = f(mid)
            if fmid == 0:
                return mid
            if (flo < 0 and fmid < 0) or (flo > 0 and fmid > 0):
                lo = mid + 1
                flo = f(lo)
            else:
                hi = mid - 1
                fhi = f(hi)
        return None

    # Critical points where df(X) = 3 X^2 + 2 B2 X + B4 = 0
    disc_df = 4 * B2 * B2 - 12 * B4
    intervals = [(-bound, bound)]
    if disc_df >= 0:
        sq = math.isqrt(disc_df)
        cp1 = (-2 * B2 - sq) // 6
        cp2 = (-2 * B2 + sq) // 6
        pts = sorted(set([-bound, cp1 - 1, cp1, cp1 + 1, cp2 - 1, cp2, cp2 + 1, bound]))
        intervals = [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]

    roots = set()
    for lo, hi in intervals:
        if lo <= hi:
            r = bisect_root(lo, hi)
            if r is not None and f(r) == 0:
                roots.add(r)
    return sorted(roots)


def velu_2isogeny(ainvs, x0, y0):
    """Apply Velu's 2-isogeny formula for 2-torsion point T = (x0, y0)."""
    a1, a2, a3, a4, a6 = [Fraction(x) for x in ainvs]
    t = 3 * x0 * x0 + 2 * a2 * x0 + a4 - a1 * y0
    u = 4 * x0 * x0 * x0 + (a1 * a1 + 4 * a2) * x0 * x0 + 2 * (2 * a4 + a1 * a3) * x0 + (a3 * a3 + 4 * a6)
    # Note: for a 2-torsion point, u == 0!
    w = u + x0 * t
    A1 = a1
    A2 = a2
    A3 = a3
    A4 = a4 - 5 * t
    A6 = a6 - (a1 * a1 + 4 * a2) * t - 7 * w
    return [A1, A2, A3, A4, A6], t


def canonical_key_from_c4_c6(c4, c6, bad_primes):
    """Compute global minimal c4:c6 key if bad_primes are known."""
    c4_i = int(c4)
    c6_i = int(c6)
    if bad_primes:
        for p_str in bad_primes:
            p = int(p_str)
            if p in (2, 3):
                continue
            p4 = p ** 4
            p6 = p ** 6
            while c4_i % p4 == 0 and c6_i % p6 == 0:
                c4_i //= p4
                c6_i //= p6
    return c4_i, c6_i


# Scan high-rank curves with torsion containing 2
candidates = []
for c in curves:
    tors = str(c.get("torsion"))
    rk = c["rank_lower_bound"]
    if rk >= 10 and any(k in tors for k in ["2", "4", "6", "8", "10", "12"]):
        B2, B4, B6, a1, a3 = find_2torsion_points(c["ainvs"])
        roots = integer_roots_monic_cubic(B2, B4, B6)
        for X in roots:
            x0 = Fraction(X, 4)
            y0 = -(a1 * x0 + a3) / 2
            new_ainvs, t_val = velu_2isogeny(c["ainvs"], x0, y0)
            _, _, _, _, c4_new, c6_new, disc_new = weierstrass_invariants(new_ainvs)
            # Check if any scale u in {1, 2, 1/2, 3, 1/3, 4, 1/4, 6, 1/6} matches an existing curve_key
            already = False
            for p_pow2 in range(-6, 7):
                for p_pow3 in range(-4, 5):
                    u = Fraction(2) ** p_pow2 * Fraction(3) ** p_pow3
                    # also strip known bad primes > 3
                    c4_s = c4_new * (u ** 4)
                    c6_s = c6_new * (u ** 6)
                    if c4_s.denominator == 1 and c6_s.denominator == 1:
                        k_str = f"{int(c4_s)}:{int(c6_s)}"
                        if k_str in existing_keys:
                            already = True
                            break
                if already:
                    break
            if not already:
                candidates.append((rk, tors, c["id"], c["submitter"], float(c.get("naive_height", 999))))

candidates.sort(key=lambda x: (-x[0], x[4]))
print(f"\nFound {len(candidates)} high-rank (rk >= 10) unsubmitted 2-isogeny candidates!")
for cand in candidates[:25]:
    print(f"  rank>={cand[0]:2d} | src_tors={cand[1]:8s} | src_curve=#{cand[2]:4d} ({cand[3]}) | src_naive={cand[4]:.2f}")
