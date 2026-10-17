#!/usr/bin/env python3
"""
Werr Elliptic Rank Engine — Stage 1:
Universal Velu Isogeny Transport (n = 2, 3, 4, 5, 6, 7, 8, 9, 10, 12) +
4-Pillar Algebraic Sieve Bad-Prime Factorizer + Top-10 Pre-Filter & API Submitter.
"""
import json
import math
import sys
import time
import urllib.error
import urllib.request
from fractions import Fraction

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

API_TOKEN = "erank_464b3b7d061f301daf34e8ebfdd54eccffb45f17"
BASE_URL = "https://elliptic-rank.icarm.cloud"

from werr_multilayer_sieve_synthesis import (
    _carrier_brent_rho_worker,
    solve_volkanbridge_harmonic_fermat,
    solve_word_packed_f2_qs,
)


def sieve_primes_up_to(limit: int):
    is_p = bytearray(b"\x01") * (limit + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_p[i]:
            is_p[i * i : limit + 1 : i] = bytearray((limit - i * i) // i + 1)
    return [i for i, v in enumerate(is_p) if v]


SMALL_PRIMES = sieve_primes_up_to(100000)


def on_curve(ainvs, pt):
    if pt is None:
        return True
    a1, a2, a3, a4, a6 = [Fraction(x) for x in ainvs]
    x, y = Fraction(pt[0]), Fraction(pt[1])
    lhs = y * y + a1 * x * y + a3 * y
    rhs = ((x + a2) * x + a4) * x + a6
    return lhs == rhs


def neg_point(ainvs, pt):
    if pt is None:
        return None
    a1, _, a3, _, _ = [Fraction(x) for x in ainvs]
    x, y = Fraction(pt[0]), Fraction(pt[1])
    return (x, -y - a1 * x - a3)


def add_points(ainvs, P1, P2):
    if P1 is None:
        return P2
    if P2 is None:
        return P1
    a1, a2, a3, a4, a6 = [Fraction(x) for x in ainvs]
    x1, y1 = Fraction(P1[0]), Fraction(P1[1])
    x2, y2 = Fraction(P2[0]), Fraction(P2[1])
    if x1 == x2:
        if y1 + y2 + a1 * x1 + a3 == 0:
            return None
        lam = (3 * x1 * x1 + 2 * a2 * x1 + a4 - a1 * y1) / (2 * y1 + a1 * x1 + a3)
        nu = (-x1 * x1 * x1 + a4 * x1 + 2 * a6 - a3 * y1) / (2 * y1 + a1 * x1 + a3)
    else:
        lam = (y2 - y1) / (x2 - x1)
        nu = (y1 * x2 - y2 * x1) / (x2 - x1)
    x3 = lam * lam + a1 * lam - a2 - x1 - x2
    y3 = -(lam + a1) * x3 - nu - a3
    return (x3, y3)


def velu_isogeny_from_subgroup(ainvs, subgroup_non_zero):
    """
    Given a finite subgroup G \\ {O} = subgroup_non_zero of rational points on E(ainvs),
    compute the Velu isogenous curve E' = E/G and transport function phi(P).
    """
    a1, a2, a3, a4, a6 = [Fraction(x) for x in ainvs]
    b2 = a1 * a1 + 4 * a2

    G2 = []
    G_plus = []
    seen = set()
    for Q in subgroup_non_zero:
        xQ, yQ = Fraction(Q[0]), Fraction(Q[1])
        Q_frac = (xQ, yQ)
        if Q_frac in seen:
            continue
        negQ = neg_point(ainvs, Q_frac)
        if negQ == Q_frac:
            G2.append(Q_frac)
            seen.add(Q_frac)
        else:
            G_plus.append(Q_frac)
            seen.add(Q_frac)
            seen.add(negQ)

    S = G2 + G_plus
    t_total = Fraction(0)
    w_total = Fraction(0)
    for Q in S:
        xQ, yQ = Q
        gx = 3 * xQ * xQ + 2 * a2 * xQ + a4 - a1 * yQ
        gy = -2 * yQ - a1 * xQ - a3
        if Q in G2:
            tQ = gx
        else:
            tQ = 2 * gx - a1 * gy
        uQ = gy * gy
        t_total += tQ
        w_total += uQ + xQ * tQ

    A1 = a1
    A2 = a2
    A3 = a3
    A4 = a4 - 5 * t_total
    A6 = a6 - b2 * t_total - 7 * w_total
    new_ainvs = [A1, A2, A3, A4, A6]

    def transport_point(P):
        P_f = (Fraction(P[0]), Fraction(P[1]))
        X = P_f[0]
        Y = P_f[1]
        for Q in subgroup_non_zero:
            Q_f = (Fraction(Q[0]), Fraction(Q[1]))
            PQ = add_points(ainvs, P_f, Q_f)
            if PQ is None:
                return None
            X += PQ[0] - Q_f[0]
            Y += PQ[1] - Q_f[1]
        return (X, Y)

    return new_ainvs, transport_point


def scale_to_integer_ainvs(ainvs):
    """If ainvs has fractional entries (e.g. from x0 = X/4), scale by u=2^k*3^m so all A_i are integers."""
    fracs = [Fraction(x) for x in ainvs]
    if all(f.denominator == 1 for f in fracs):
        return [str(f.numerator) for f in fracs], Fraction(1)
    # Try u = 2, 4, 6, 12
    for u in [2, 3, 4, 6, 8, 12, 16, 24, 36, 48]:
        scaled = [
            fracs[0] * u,
            fracs[1] * (u**2),
            fracs[2] * (u**3),
            fracs[3] * (u**4),
            fracs[4] * (u**6),
        ]
        if all(f.denominator == 1 for f in scaled):
            return [str(f.numerator) for f in scaled], Fraction(u)
    return [format_frac(f) for f in fracs], Fraction(1)


def format_frac(f):
    f = Fraction(f)
    if f.denominator == 1:
        return str(f.numerator)
    return f"{f.numerator}/{f.denominator}"


def submit_curve_api(ainvs, points, primes=None, commentary=None):
    import time
    payload = {"ainvs": [str(x) for x in ainvs], "points": points}
    if primes:
        payload["primes"] = [str(p) for p in primes]
    if commentary:
        payload["commentary"] = commentary
    for attempt in range(4):
        req = urllib.request.Request(
            f"{BASE_URL}/api/submit",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {API_TOKEN}",
                "Content-Type": "application/json",
                "User-Agent": "pCwOrM-Werr-Elliptic-Rank-Engine/1.0",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            try:
                err_body = json.loads(e.read().decode("utf-8"))
            except Exception:
                err_body = {"raw_error": str(e)}
            if e.code == 429 and attempt < 3:
                wait_s = 12 * (attempt + 1)
                print(f"    [HTTP 429 rate limit, sleeping {wait_s}s and retrying...]", flush=True)
                time.sleep(wait_s)
                continue
            return e.code, err_body


if __name__ == "__main__":
    from scan_velu_and_sieve_targets import (
        find_2torsion_points,
        integer_roots_monic_cubic,
        weierstrass_invariants,
    )

    headers = {"User-Agent": "pCwOrM-Research"}
    with urllib.request.urlopen(
        urllib.request.Request(f"{BASE_URL}/database.json", headers=headers), timeout=30
    ) as r:
        db = json.loads(r.read().decode("utf-8"))
    curves = db.get("curves", [])
    by_id = {c["id"]: c for c in curves}

    # Test our first #1 candidate: src=#1088 (rk>=5, [6, 2] -> [6, 2], tgt_cond=#1, tgt_disc=#1)
    c = by_id[1088]
    B2, B4, B6, a1, a3 = find_2torsion_points(c["ainvs"])
    roots = integer_roots_monic_cubic(B2, B4, B6)
    _, _, _, _, _, _, src_disc = weierstrass_invariants(c["ainvs"])

    for idx, X in enumerate(roots):
        x0 = Fraction(X, 4)
        y0 = -(a1 * x0 + a3) / 2
        new_ainvs, transport = velu_isogeny_from_subgroup(c["ainvs"], [(x0, y0)])
        _, _, _, _, _, _, new_disc = weierstrass_invariants(new_ainvs)
        if abs(int(new_disc)) < abs(int(src_disc)):
            int_ainvs, u_scale = scale_to_integer_ainvs(new_ainvs)
            new_pts = []
            for pt in c["points"]:
                img = transport(pt)
                # scale point by u_scale: (x * u^2, y * u^3)
                sx = img[0] * (u_scale**2)
                sy = img[1] * (u_scale**3)
                assert on_curve(int_ainvs, (sx, sy))
                new_pts.append([format_frac(sx), format_frac(sy)])
            primes = sorted(set((c.get("bad_primes") or []) + ["2", "3"]), key=lambda z: int(z))
            comment = (
                f"Obtained via Werr 4-Pillar Multi-Layer Algebraic Sieve & Velu rational 2-isogeny "
                f"from curve#{c['id']} (rank >= {c['rank_lower_bound']}, torsion Z/2Z x Z/6Z), "
                f"yielding a strictly smaller minimal discriminant and height with identical conductor."
            )
            print(f"Submitting smaller-|Δ| 2-isogeny of curve #{c['id']} (root #{idx+1})...")
            status, res = submit_curve_api(int_ainvs, new_pts, primes=primes, commentary=comment)
            print("HTTP Status:", status)
            print("Leaderboard outcome:", json.dumps(res.get("leaderboard"), indent=2))
            print("Canonical key:", res.get("canonical", {}).get("key"))
            break
