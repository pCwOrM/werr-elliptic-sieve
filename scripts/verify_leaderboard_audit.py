#!/usr/bin/env python3
"""
Exact audit of Volkan Dagli's (user/114) 230 curves (#4308..#4537) across every leaderboard table on
https://elliptic-rank.icarm.cloud:
1. Main Overall Leaderboard (all curves with rank >= r, ordered by Conductor N, Discriminant |Δ|, Faltings height, Naive height).
2. Torsion-Specific Leaderboards (curves with torsion == T and rank >= r, ordered by all 4 metrics).
3. Overall contributor rankings across the entire database!
"""
import json
import math
import re
import sys
import urllib.request
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_URL = "https://elliptic-rank.icarm.cloud"
headers = {"User-Agent": "pCwOrM-Research"}

with urllib.request.urlopen(urllib.request.Request(f"{BASE_URL}/database.json", headers=headers), timeout=30) as r:
    db = json.loads(r.read().decode("utf-8"))

curves = db.get("curves", [])
by_id = {c["id"]: c for c in curves}

with urllib.request.urlopen(urllib.request.Request(f"{BASE_URL}/user/114", headers=headers), timeout=20) as r:
    u_html = r.read().decode("utf-8", errors="replace")

our_ids = set(int(x) for x in re.findall(r'data-id="(\d+)"', u_html))
print(f"Total curves in live DB: {len(curves)} | Volkan Dagli (/user/114) curves: {len(our_ids)}")

# Check data-rec and data-trec on /user/114 HTML!
# Wait: on /user/114, each metric cell has data-rec="1" if it's #1 overall or in Top 10! Let's inspect!
rec_matches = re.findall(r'<tr data-id="(\d+)"[^>]*>(.*?)</tr>', u_html, re.DOTALL)
html_rec_count = 0
html_trec_count = 0
for cid_s, row_html in rec_matches:
    recs = re.findall(r'data-rec="(\d+)"\s+data-trec="(\d+)"', row_html)
    if any(r != "0" for r, _ in recs):
        html_rec_count += 1
    if any(tr != "0" for _, tr in recs):
        html_trec_count += 1
print(f"Rows on /user/114 with non-zero data-rec: {html_rec_count}, data-trec: {html_trec_count}")


def metric_val(c, m):
    if m == "cond":
        cond = c.get("conductor")
        return int(cond) if cond else float("inf")
    if m == "disc":
        d = c.get("discriminant")
        return abs(int(d)) if d else float("inf")
    if m == "faltings":
        fh = c.get("faltings_height")
        return float(fh) if fh is not None else float("inf")
    if m == "naive":
        nh = c.get("naive_height")
        return float(nh) if nh is not None else float("inf")
    return float("inf")


metrics = ["cond", "disc", "faltings", "naive"]
metric_names = {"cond": "Conductor (N)", "disc": "Discriminant |Δ|", "faltings": "Faltings Height", "naive": "Naive Height"}

# 1. MAIN OVERALL LEADERBOARD (rank >= r, across ALL curves regardless of torsion!)
print("\n=== 1. MAIN OVERALL LEADERBOARD PLACEMENTS (TOP 10 ACROSS ALL CURVES FOR RANK >= r) ===")
main_top10_summary = []
for r in range(28, 3, -1):
    pool = [c for c in curves if c["rank_lower_bound"] >= r]
    if not pool:
        continue
    cell_hits = {}
    for m in metrics:
        ranked = sorted(pool, key=lambda c: metric_val(c, m))[:10]
        our_pos = [(idx + 1, c["id"]) for idx, c in enumerate(ranked) if c["id"] in our_ids and metric_val(c, m) < float("inf")]
        if our_pos:
            cell_hits[m] = our_pos
    if cell_hits:
        main_top10_summary.append((r, cell_hits))
        print(f"  Rank >= {r:2d}:")
        for m, pos_list in cell_hits.items():
            pos_str = ", ".join(f"#{pos} (curve #{cid})" for pos, cid in pos_list)
            print(f"    - {metric_names[m]:18s}: {len(pos_list)}/10 in Top 10 -> {pos_str}")

# 2. TORSION SUBGROUP LEADERBOARDS (torsion == T and rank >= r)
print("\n=== 2. TORSION SUBGROUP LEADERBOARD PLACEMENTS (TOP 10 FOR TORSION == T, RANK >= r) ===")
all_torsions = sorted(set(str(c["torsion"]) for c in curves))
torsion_top10_cells = 0
total_top1_placements = 0
total_top3_placements = 0
total_top10_placements = 0

for t in all_torsions:
    t_curves = [c for c in curves if str(c["torsion"]) == t]
    max_r = max(c["rank_lower_bound"] for c in t_curves)
    for r in range(max_r, 3, -1):
        pool = [c for c in t_curves if c["rank_lower_bound"] >= r]
        if not pool:
            continue
        cell_hits = {}
        for m in metrics:
            ranked = sorted(pool, key=lambda c: metric_val(c, m))[:10]
            our_pos = [(idx + 1, c["id"]) for idx, c in enumerate(ranked) if c["id"] in our_ids and metric_val(c, m) < float("inf")]
            if our_pos:
                cell_hits[m] = our_pos
                for pos, _ in our_pos:
                    total_top10_placements += 1
                    if pos == 1:
                        total_top1_placements += 1
                    if pos <= 3:
                        total_top3_placements += 1
        if cell_hits:
            torsion_top10_cells += 1
            print(f"  Torsion {t:8s} | Rank >= {r:2d}:")
            for m, pos_list in cell_hits.items():
                pos_str = ", ".join(f"#{pos} (#{cid})" for pos, cid in pos_list)
                print(f"    - {metric_names[m]:18s}: {len(pos_list)}/10 -> {pos_str}")

print(f"\n=== SUMMARY OF MEDAL & TOP-10 PLACEMENTS ACROSS ALL TORSION LEADERBOARDS ===")
print(f"  Active (Torsion, Rank) Leaderboards with Volkan Dagli in Top 10: {torsion_top10_cells}")
print(f"  Total #1 (Gold / Record) Metric Placements: {total_top1_placements}")
print(f"  Total Top-3 (Podium) Metric Placements:     {total_top3_placements}")
print(f"  Total Top-10 Metric Placements:             {total_top10_placements}")
