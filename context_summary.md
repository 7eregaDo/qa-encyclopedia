# QA Encyclopedia — Project Context v2

## 1. Project Overview
A Jekyll-based static site using Collections to organise QA interview prep content across 10 modules and 4 seniority levels.

---

## 2. Technical Stack
- **Framework:** Jekyll (Static Site Generator)
- **Data Model:** Jekyll Collections
- **Collection Name:** `_questions`
- **Directory Structure:** `_questions/{category}/{level}/q{id}.md`
- **Configuration:** `_config.yml` must have `collections.questions.output: true`

---

## 3. Content Standard ("Claude Style")
Every question is a standalone Markdown file. Structure is strictly enforced.

### Front Matter (required fields)
```yaml
---
question_id: (Integer)
title: (String) The interview question
category: (String) module name
level: (String) entry | mid | senior | lead
theory: (String) A brief, formal definition of the concept
---
```

### Body Structure (required sections, in order)
1. `## The Intent` — Why the interviewer is asking this
2. `## The STAR Script` — Situation, Task, Action, Result (concrete, realistic)
3. `## Seniority Shift` — Table showing depth expected at Entry / Mid / Senior / Lead
4. `## Key Terms` — Table of definitions (6–9 rows typically)

### Quality Standards
- STAR scripts must be specific and technical — not generic
- Seniority Shift tables must have 4 rows for modules with Lead level, 3 rows for others
- Key Terms tables use `| Term | Definition |` format
- Theory field is a single formal sentence in front matter (not a heading in body)

---

## 4. Level Definitions

| Level | Focus |
|-------|-------|
| **Entry** | Individual execution, fundamentals, definitions |
| **Mid** | Process ownership, decision-making, cross-functional collaboration |
| **Senior** | Strategy, technical architecture, data-driven influence |
| **Lead** | Org-wide vision, team building, executive partnership, culture at scale |

---

## 5. Modules & Levels

Lead level applies to: **behavioral**, **manual-testing**, **automation** (confirmed). For other modules, Lead level TBD as we reach them.

| # | Module | Levels |
|---|--------|--------|
| 1 | qa-theory | entry, mid, senior |
| 2 | behavioral | entry, mid, senior, **lead** |
| 3 | manual-testing | entry, mid, senior, **lead** |
| 4 | automation | entry, mid, senior, **lead** |
| 5 | system-design | entry, mid, senior (lead TBD) |
| 6 | api-testing | TBD |
| 7 | ci-cd | TBD |
| 8 | security-testing | TBD |
| 9 | performance-testing | TBD |
| 10 | data-ai-testing | TBD |

---

## 6. Progress Tracker

| Module | Level | IDs | Status |
|--------|-------|-----|--------|
| qa-theory | entry | q1–q10 | ✅ Done |
| qa-theory | mid | q11–q20 | ✅ Done |
| qa-theory | senior | q21–q30 | ✅ Done |
| behavioral | entry | q31–q40 | ✅ Done |
| behavioral | mid | q41–q50 | ✅ Done |
| behavioral | senior | q51–q60 | ✅ Done |
| behavioral | lead | q61–q70 | ✅ Done |
| manual-testing | entry | q71–q80 | ✅ Done |
| manual-testing | mid | q81–q90 | ✅ Done |
| manual-testing | senior | q91–q100 | ✅ Done |
| manual-testing | lead | q101–q110 | ✅ Done |
| automation | entry | q111–q120 | ✅ Done |
| automation | mid | q121–q130 | ✅ Done |
| automation | senior | q131–q140 | ✅ Done |
| automation | lead | q141–q150 | ✅ Done |
| system-design | entry | q151–q160 | ✅ Done |
| system-design | mid | q161–q170 | ✅ Done |
| system-design | senior | q171–q180 | ⏳ Next |
| api-testing | all levels | — | ⬜ Pending |
| ci-cd | all levels | — | ⬜ Pending |
| security-testing | all levels | — | ⬜ Pending |
| performance-testing | all levels | — | ⬜ Pending |
| data-ai-testing | all levels | — | ⬜ Pending |

**Next question ID to use: q171**

---

## 7. Filtering Logic (Jekyll)
Level pages use Liquid to filter the collection:
```liquid
site.questions | where: "category", "automation" | where: "level", "senior"
```
Dynamic cards rendered via `_includes/question_card.html` using `question_id`.

---

## 8. Working Instructions for New Chat

### Streamlined workflow (leaner, cheaper):
1. **No approval round** — go straight from "next please" to full implementation
2. **No file presentation step** — files go directly to `/mnt/user-data/outputs/{module}/{level}/q{id}.md` and user copies from the output folder
3. **Still produce all 10 questions per level per message** — quality and structure unchanged
4. **End each batch** with a brief tracker update (the table above, updated)

### File output path pattern:
```
/mnt/user-data/outputs/{category}/{level}/q{id}.md
```
Example: `/mnt/user-data/outputs/system-design/senior/q171.md`

### To continue from where we left off:
Start with **system-design / senior** — 10 questions, IDs q171–q180.

After that, continue in module order:
- system-design / lead (TBD whether lead applies)
- api-testing / entry → mid → senior → lead (TBD)
- ci-cd / entry → mid → senior → lead (TBD)
- security-testing / entry → mid → senior → lead (TBD)
- performance-testing / entry → mid → senior → lead (TBD)
- data-ai-testing / entry → mid → senior → lead (TBD)

---

## 9. Example File (for reference)

```markdown
---
question_id: 11
title: "What is risk-based testing, and how do you decide what to test first?"
category: qa-theory
level: mid
theory: "Risk-based testing is a test strategy that prioritises testing activities based on the likelihood and impact of potential failures."
---

## The Intent
...

## The STAR Script
**Situation:** ...
**Task:** ...
**Action:** ...
**Result:** ...

## Seniority Shift
| Level | Expected Depth |
|-------|---------------|
| **Entry** | ... |
| **Mid** | ... |
| **Senior** | ... |

## Key Terms
| Term | Definition |
|------|------------|
| **Risk-Based Testing** | ... |
```