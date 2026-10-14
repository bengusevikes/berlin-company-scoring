"""
Apply the two spot-check fixes from the decision log (D19) to the Clay export
and write the public, company-level result.

Input:  private/clay_export_raw.csv   (Clay export, 200 companies)
Output: data/scored_companies.csv     (199 companies, company-level columns only)

Fixes:
1. Hiring GTM ignores job titles that contain "marketing"
   (the keyword "Growth" had matched marketing roles).
2. "Pile (part of Vivid Money)" is removed: it is the same company as Vivid.

The score and tier rules are the same as in Clay (D18).
"""

import csv
import re

DUPLICATES = {"Pile (part of Vivid Money)"}

PUBLIC_COLUMNS = [
    "Name", "Domain", "Industry", "Size", "Sector",
    "Funded", "Hiring GTM", "Title Jobs", "Job Language",
    "Has RevOps/GTM person", "Percent Employee Growth Over Last 12 Months", "Growing",
    "Score", "Tier",
]


def hiring_gtm(title):
    title = (title or "").strip()
    return "Yes" if title and not re.search(r"marketing", title, re.I) else "No"


def score(row):
    return (
        (25 if row["Hiring GTM"] == "Yes" else 0)
        + (25 if row["Has RevOps/GTM person"] == "Yes" else 0)
        + (20 if row["Funded"] == "Yes" else 0)
        + (15 if row["Growing"] == "Yes" else 0)
        + (15 if row["Sector"] in ("Fintech", "B2B SaaS") else 5)
    )


def tier(row):
    if row["Type"] == "Non Profit" or row["Job Language"] == "German":
        return "Excluded"
    s = row["Score"]
    return "A" if s >= 70 else "B" if s >= 50 else "C"


with open("private/clay_export_raw.csv", encoding="utf-8-sig", newline="") as f:
    rows = [r for r in csv.DictReader(f) if r["Name"] not in DUPLICATES]

for r in rows:
    r["Hiring GTM"] = hiring_gtm(r["Title Jobs"])
    r["Score"] = score(r)
    r["Tier"] = tier(r)

rows.sort(key=lambda r: (-r["Score"], r["Name"].lower()))

with open("data/scored_companies.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=PUBLIC_COLUMNS, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

counts = {}
for r in rows:
    counts[r["Tier"]] = counts.get(r["Tier"], 0) + 1
print(f"{len(rows)} companies:", ", ".join(f"{t} {counts.get(t, 0)}" for t in ["A", "B", "C", "Excluded"]))
