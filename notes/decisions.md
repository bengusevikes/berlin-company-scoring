# Decision log: Berlin startup scoring

A running log of every decision in this project and why I made it. Status: **confirmed** (decided) or **proposed** (still open).

---

## Context: what this project is

A scored target account list of Berlin tech startups, built the way a GTM engineer builds one: clear criteria, sourcing, enrichment, a scoring model and tiers. I used my own criteria for a good employer as the ICP, so every decision is one I can explain from first-hand reasoning.

The criteria:
- Based in Berlin
- English as the working language
- Tech, ideally fintech or B2B SaaS
- A team to learn from
- Room to grow into new responsibilities

---

## D1. Starting criteria (14 Oct 2026) · confirmed

Berlin-based, English-speaking, tech company. Employee size can be anything. Sector: fintech or B2B SaaS, but open to other tech.

## D2. Split criteria into filters and scoring (14 Oct 2026) · confirmed

**Decision:** Berlin, English and tech are filters (yes/no). A company that fails any of them is removed. Everything else is scored.

**Why:** My first criteria were all yes/no. That gives a list, not a ranking. Filters decide who's in; the score decides the order.

## D3. Measure team structure directly instead of company size (14 Oct 2026) · confirmed

**Decision:** No size score. Instead, score whether the company already has someone in RevOps, GTM or Sales Ops.

**Why:** Size is a weak proxy for what I care about, which is an existing team and processes to learn from. A small startup can have a strong RevOps lead; a large company can have none. So I measure the team directly.

## D4. English as a working language: proxy (14 Oct 2026) · confirmed

**Decision:** A company passes if its job postings are written in English.

**Why:** No data provider has a reliable "working language" field. English job posts are the closest public signal.

**Limitation:** Some companies post in English but run sales or client work in German. Tier A companies get a manual spot-check.

## D5. Scoring signals and weights (14 Oct 2026) · confirmed

| Signal | Why it matters | Points |
|---|---|---|
| Hiring for GTM / RevOps / Ops roles | The company is building out its GTM function right now | 25 |
| Has a RevOps / GTM / Sales Ops person | There's an existing team and processes to learn from | 25 |
| Raised in the last 24 months, or Series A+ | More budget for GTM tooling and people | 20 |
| Headcount growing over the last 12 months | More room to take on new scope | 15 |
| Fintech or B2B SaaS (other tech = 5) | The sectors I'm most interested in | 15 |

**Why equal weights for the top two:** I considered weighting "hiring now" higher, but an active GTM build-out and an existing team to learn from matter equally. Neither alone makes a company a great fit.

Tiers: A = 70+, B = 50–69, C = below 50.

## D6. One source: Clay company search (14 Oct 2026) · confirmed

**Decision:** All companies come from Clay's company search.

**Options I considered and dropped:**
- Starting from a list of companies I'd collected by hand. Dropped because finding the companies is part of the skill this project should show.
- Adding a second source (a public list of startups funded in 2026) and using my hand-picked list as a benchmark for sourcing quality. Dropped to keep the scope to one finished project. Both are listed under "What I'd do next".

## D7. What goes public (14 Oct 2026) · confirmed

**Decision:** Company-level data (names, scores, tiers) can be public. Anything about individual people (names, emails, LinkedIn profiles) stays in a private folder that never goes to GitHub.

## D8. Narrowing the Clay search: headquarters in Berlin (14 Oct 2026) · confirmed

**Starting point:** Clay search for Berlin + tech industries returned **10,904 companies**.

**What the results showed:** The top of the list was mostly large global companies with a Berlin office (e.g. Snap, Semrush, Verizon Business) and IT outsourcing or consulting firms (e.g. Endava, SoftServe, Reply).

**Decision:**
1. **Headquarters in Berlin, not just an office.** "Based in Berlin" means the company is run from here. A sales office of a US company is a different kind of workplace.
2. **Remove "IT Services and IT Consulting".** These are mostly service and outsourcing firms. I want companies that build and sell their own product.

**What broke on the first try:** I added "location is headquarters" and "location is Berlin" as two separate conditions. Clay checks each one on its own, so a company passed if it had *any* headquarters and *any* Berlin office. Google (HQ in Mountain View, office in Berlin) passed both. The count only fell from 10,904 to 6,170, and the top results were still US companies. Fix: both conditions inside the same location rule, i.e. "a location that is the headquarters **and** is in Berlin".

**After the fix:** **5,037 companies**, and the top results looked right: companies actually run from Berlin (e.g. n8n, N26, Parloa, Qdrant). Some noise remained (a savings bank, a recruitment agency tagged as software). The tech filter after enrichment will catch these.

## D9. Startups only: 11–500 employees (14 Oct 2026) · confirmed

**Update to D1:** I started with "size can be anything", but what I actually want is a startup or scale-up, not a large corporation. So size becomes a sourcing filter after all.

**Decision:** Source companies with 11–500 employees.

**Why this range:**
- **Up to 500:** Above that, a company usually stops feeling like a startup. 201–500 stays in because these scale-ups are the most likely to already have a RevOps or GTM team, which is the "team to learn from" signal in the score.
- **From 11:** I first kept 2–10 as well, to include the earliest-stage startups. I dropped them because companies that small almost never have a GTM team or any structure yet. They would land in Tier C anyway, so enriching them would use credits for nothing.
- **11–50 stays in:** Early-stage startups are where the first GTM hires happen.

**Relation to D3:** Size is still not part of the score. It only decides which companies get sourced.

**Count:** 5,037 → **1,496 companies.**

## D10. Sector keywords in the description (14 Oct 2026) · confirmed

**Decision:** Keep only companies whose description contains at least one of: B2B, SaaS, enterprise, businesses, fintech, payments, banking, finance.

**Why:**
- B2B, SaaS, enterprise and businesses target companies that sell to other companies. GTM Engineer and RevOps roles exist mostly at B2B companies.
- fintech, payments, banking and finance keep consumer fintechs in (e.g. N26, Trade Republic), because fintech is one of my two preferred sectors.

**Trade-off:** Keyword matching misses companies that describe themselves differently.

**Count:** 1,496 → **593 companies.**

**Sourcing funnel:** 10,904 (Berlin + tech) → 6,170 (first HQ attempt, logic bug) → 5,037 (HQ in Berlin) → 1,496 (11–500 employees) → 593 (sector keywords).

## D11. Work within the 200-row table limit (14 Oct 2026) · confirmed

**What happened:** Importing the 593 companies into a Clay table stopped at 200. My Clay plan caps each table at 200 rows.

**Decision:** Use these 200 instead of upgrading.

**Limitation:** Clay chose *which* 200 of the 593 to import, in its own default order, not by a rule of mine. The list seems to lean toward better-known companies.

**Plan for enrichment:** Test every column on 10 rows before running all 200. Run the cheap signals first; only spend more (finding a contact person, tech stack) on companies that score well.

## D12. Credit budget: free columns first (14 Oct 2026) · confirmed

**Constraint:** My Clay plan has about 180 credits. Enriching 200 companies across five signals would need far more.

**Decision:** Order the work by cost.
1. **Free:** formula columns built on data that came with the search (description, industry, size).
2. **Paid, on fewer rows:** funding and headcount, only for companies that pass the free filters.
3. **Most expensive, on the top group only:** finding the RevOps/GTM person.

Before each paid column I note Clay's cost per row and decide how many rows it can run on.

## D13. Sector tag with a formula, not AI (14 Oct 2026) · confirmed

**Decision:** A free formula column tags each company by keywords in its description:
- fintech, payment, banking, finance, financial → **Fintech**
- saas, b2b, enterprise, businesses → **B2B SaaS**
- anything else → **Other**

**Why:** An AI column would read descriptions more accurately, but it costs credits on every row. Keywords are good enough to sort 200 companies into three buckets, and they cost nothing.

**Known weakness:** Fintech is checked first, so a B2B SaaS tool for finance teams is tagged Fintech. That's acceptable, since both sectors score the same 15 points.

**What broke on the first try:** I spot-checked the first 11 rows and 5 were wrong. n8n, JOIN, Qdrant and Choco were tagged "Other", although all four sell software to businesses; their descriptions just don't use words like "SaaS" or "B2B". Plan A (climate software) was tagged "Fintech", most likely because its description mentions finance.

**Fix:** Use the Industry column as the main signal and keep keywords only as a backup for fintech:
- Industry is Financial Services, Banking or Insurance, **or** the description mentions fintech, payment or banking → **Fintech**
- Otherwise, industry is Software Development → **B2B SaaS**
- Anything else → **Other**

**Lesson:** Companies don't describe themselves in the words a filter expects. A structured field (industry) beats free-text keywords for broad categories.

**Remaining weakness:** "Software Development" also covers consumer apps (e.g. a mobility app), which now get tagged B2B SaaS.

**Result after the fix:** On the same 11 rows, 10 are now tagged correctly. The one miss is MOIA (a mobility service), tagged B2B SaaS, which is the known weakness above.

## D14. Funding: a free lookup instead of paid enrichment (14 Oct 2026) · confirmed

**What I found:** Clay's "Latest Funding" waterfall costs ~6.4 credits per row. Single providers cost 3 (Intellizence, AI), 4 (Dealroom), 10 (Crunchbase) or 12 (CB Insights). Even the cheapest would need 600 credits for 200 companies; I have ~180.

**Decision:** Build my own funding list from free public sources and check each company against it with a formula (0 credits):
- The Berlin Life: Berlin startups funded in 2026 (120 companies)
- Silicon Canals: Berlin funding roundup for October 2025
- Growth List and LeadMagic: a few Berlin rounds from November and December 2025

Result: 137 Berlin companies with a known round between October 2025 and September 2026.

**How the match works:** Company names are normalized before comparing (lowercase, legal suffixes like GmbH/SE/AG removed, punctuation removed), so "Upvest" matches "Upvest GmbH".

**Limitation:** My scoring signal asks for funding in the last 24 months. I looked for free lists covering 2024 and 2025 but only found partial coverage from October 2025. Companies that raised in 2024 or early 2025 will show "No" even if they did raise. With a bigger budget, a paid funding column would close this gap.

**Why it's still worth it:** Credits are kept for the signals with no free alternative (job postings, the RevOps/GTM person).

**Result:** **10 of 200 companies (5%)** matched a known recent round. Some well-funded fintechs (e.g. Billie, Pliant, Payrails) show "No", most likely because their rounds fall in 2024 or early 2025, outside the free list's coverage.

**What this means for scoring:** With 5% coverage, the 20-point funding signal will rarely score. It tells me "this company is on my list" more than "this company raised money". I'll keep the column and decide on its weight once all signals are in and I can see the score distribution.

## D15. Hiring signal: Clay's job openings enrichment (14 Oct 2026) · confirmed

**Options compared:**

| Option | Cost per row | 200 rows |
|---|---|---|
| Find active job openings (Clay) | 0.5 | 100 |
| Find open jobs (PredictLeads) | 0.5 | 100 |
| Company Job Openings (waterfall, 4 providers) | ~2 | 400 |

**Decision:** Clay's single-provider option at 0.5 credits per row. The waterfall would find more jobs, but at four times the price.

**Budget plan:** Jobs on all 200 companies = 100 credits. That leaves ~80 for "Find contacts at company" (also 0.5 per row), enough for about 160 companies.

**Test first:** 10 rows (5 credits) to see what the output contains before running all 200.

**Settings:** Company identified by domain. No job title keywords, so the same result answers two questions: "hiring for GTM/RevOps?" and "are job posts in English?" (D4). Only jobs posted in the last 60 days, max 10 per company (Clay allows 1–10; my first setting of 25 failed with "Input limit is invalid"). Auto-run off, so nothing runs on all 200 rows by accident.

**Test set:** The 10 companies with a recent funding round (the rows visible under that filter).

**Test result (10 companies, all job titles):** n8n, Qdrant, Moss, Upvest and GeneralMind returned 10 jobs (the cap). LiveEO 8, SPREAD AI 6, Plato 4, Cortea 4, Arbio 2. All visible titles were in English.

**Problem:** Half the companies hit the 10-job cap, so a GTM role could be hidden among the jobs I can't see.

**Proposed change:** Search only for GTM-related titles (GTM, Go-to-Market, RevOps, Revenue Operations, Sales Operations, Business Operations, Growth). Then any result means "hiring for GTM", and the cap stops mattering. English is checked on those GTM postings only; companies with no GTM openings get "English: unknown" rather than being filtered out.

**Test with GTM keywords (same 10 companies):** 3 of 10 have a matching opening: Qdrant (Growth Marketing Manager), GeneralMind (Growth Associate, CEO office), Arbio (GTM Intern, Founder's office). Each company now returns at most one matching job, so the cap no longer matters.

**Known weakness:** "Growth" also matches marketing roles (e.g. Growth Marketing Manager). These are GTM-adjacent but not RevOps. I kept the keyword rather than keep tuning, and I note it here.

**What the narrower search also drops:** Sales roles such as Account Executive or Sales Enablement no longer count as a hiring signal. That's intended: the signal is about GTM operations roles, not sales headcount.

**Full run (200 companies):** **18 companies** have an open GTM-related role.

**Credits:** Balance went from ~180 to 166, about 14 credits for 28 results (10 test + 18). Clay appears to charge only when it finds a job; "No Job Found" rows seem to be free. To confirm.

**Job language:** Of the 18 GTM openings, **17 have English titles and 1 has a German title**. The language check is a formula: a title containing typical German job words (e.g. Werkstudent, Vertrieb, Leiter, Mitarbeiter) counts as German; otherwise English. Companies without a GTM opening are "Unknown".

## D16. "Has a RevOps/GTM person": Clay search plus a strict title check (14 Oct 2026) · confirmed

**Setup:** Clay's "Find contacts at company" (0.5 credits per row), searching for RevOps, Revenue Operations, Sales Operations, GTM, Go-to-Market and Business Operations. Limit 1 person per company. Only the job title is added to the table, no names.

**Test (10 companies):** All 10 returned a person, but only about 6 were real matches (e.g. Revenue Operations Lead, Revenue Operations Manager, Senior Business Operations). The misses: a founder, a "Go-To-Market Advisor" (an advisor, not on the team) and an "Operations Manager" (general operations, not RevOps).

**Why:** Clay's search is fuzzy and returns someone even when the job title doesn't really fit.

**Fix:** A free formula re-checks the returned title. It counts as "Yes" only if the title contains a RevOps/GTM term **and** isn't an advisor, founder, investor or board role.

**Lesson:** An enrichment returning a result doesn't mean the result is right. A cheap second check on the output catches most false positives.

**After the fix:** The three false matches (founder, advisor, general operations manager) now show "No".

**Full run (200 companies):** Credits went from 166 to 115.5 (50.5 credits), so Clay returned a person for about **101 companies**. After the strict title check, **63 companies** have a RevOps/GTM person. The check removed about 38 loose matches, roughly 4 in 10.

**Credits:** This confirms Clay charges only when a result is found (0.5 per hit), not per row.

## D17. Headcount growth signal (14 Oct 2026) · confirmed

**Options compared:**

| Option | Cost |
|---|---|
| Find company headcount growth (Clay) | 0.5 per row |
| Employee Count (waterfall) | ~2.8 per row |
| Company Headcount Growth (waterfall) | ~4.3 per row |
| Find company headcount growth signal (Lusha) | 8 per result |

**Decision:** Clay's single-provider option at 0.5. With 115.5 credits left, it fits all 200 companies even if every row is charged.

**Test (10 companies), 12-month headcount change:** from +319% (n8n) to −19% (Moss). Others: Qdrant +53%, MOIA +28%, Vivid +28%, JOIN +16%, JustRelate +6%, Uberall −1%, Plan A −11%. Choco had no data.

**Decision: "growing" means +10% or more over 12 months.**

**Why a threshold, not "above 0%":** Small changes like +6% or −1% are usually a few hires or departures. That's noise, not growth. At +10% a team is clearly expanding.

**Missing data counts as "No".** It means "unknown", and the score shouldn't reward a company for data I don't have.

**Full run (200 companies):** Headcount data found for **186 of 200 companies (93%)**. **67 companies** grew 10%+ over 12 months.

## D18. Score and tiers (14 Oct 2026) · confirmed

**Score (0–100):** Hiring GTM 25 + Has RevOps/GTM person 25 + Funded recently 20 + Growing 15 + Sector (Fintech or B2B SaaS 15, other 5).

**Filters, applied before tiers:**
- Non-profits are excluded (e.g. a banking association that came in through the "Banking" industry).
- Companies whose GTM job posts are in German are excluded (the English filter from D2/D4).

**Tiers:** A = 70+, B = 50–69, C = below 50.

**Signal counts going in:** Hiring GTM 18 · RevOps/GTM person 63 · Funded recently 10 · Growing 67.

**Result (200 companies):**

| Tier | Companies | Share |
|---|---|---|
| A (70+) | 12 | 6% |
| B (50–69) | 22 | 11% |
| C (below 50) | 158 | 79% |
| Excluded | 8 | 4% |

**Reading the distribution:** Most companies land in C because the two strongest signals are rare: only 18 companies are hiring for a GTM role right now. That's intended. The point of the model is a short, sharp top tier, not a flattering spread.

**Funding weight (revisited):** In D14 I said I'd decide on the funding weight once I saw the distribution. I'm keeping it at 20. The tiers already separate well, and with only 10 companies matched, lowering it wouldn't change much.

**Next:** Manual spot-check of the 12 Tier A companies (does each one look like a real fit, and do they really work in English, per D4).

## D19. Spot-check of Tier A and two fixes (14 Oct 2026) · confirmed

**What I checked:** The 12 Tier A companies and all 18 hiring matches, by reading the actual job titles.

**Finding 1: "Growth" pulls in marketing roles.** 4 of the 18 hiring matches are marketing jobs (e.g. "Growth Marketing Manager", "Senior Growth Product Marketing Manager"). 3 of them were in Tier A. This is the weakness noted in D15, now with a measurable effect.

**Finding 2: one company counted twice.** "Pile (part of Vivid Money)" and "Vivid" share the same job posting and the same growth figure. Clay lists them as separate companies.

**Finding 3: a direct hit can still land in C.** One company is hiring a "Revenue Operations Specialist", exactly the target role, but scores 40 (Tier C) because its other signals are missing. Not fixed; see "What I'd do next".

**Proposed fixes:**
- Hiring GTM ignores titles containing "marketing".
- Remove the duplicate (Pile).

**Expected effect (calculated from the export):** A 12 → 9, B 22 → 23, C 158 → 159, Excluded 8.

**Also noticed:** Some matched jobs are not based in Berlin (e.g. a US role, a remote New York/London role). The job search had no location filter, so the hiring signal means "hiring for GTM somewhere", not necessarily in Berlin.

**Excluded companies (8):** 7 non-profits (mostly banking associations) and 1 company whose only GTM-matched posting was a German working-student role (which was also an HR operations job the keyword search picked up loosely).

**Result after both fixes (applied in Clay and in `scripts/apply_spotcheck_fixes.py`, same outcome):** 199 companies. **A 9 · B 23 · C 159 · Excluded 8.**
