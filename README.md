# QA Encyclopedia

> A free, open-source knowledge base of 300+ QA interview questions — structured by domain and seniority level, with model answers, seniority guides, and key term definitions.

🔗 **[Live Site → 7eregaDo.github.io/qa-encyclopedia](https://7eregaDo.github.io/qa-encyclopedia)**

---

## Why this exists

Most QA interview prep resources give you a question and a one-line answer. They don't tell you:

- What the interviewer is actually testing for
- What a **Senior** answer looks like versus a **Mid** answer
- Which terms you need to know and what they mean

The QA Encyclopedia fixes that.

---

## What's inside

Every question includes:

| Section | What it gives you |
|---|---|
| **The Intent** | What the interviewer is really probing for |
| **STAR Answer** | A full model answer using a real-world scenario |
| **Seniority Shift** | A table showing Entry / Mid / Senior / Lead answer depth |
| **Key Terms** | Every relevant term defined clearly |

---

## Domains covered

| Domain | Levels | Questions |
|---|---|---|
| 🧠 Behavioural | Entry → Lead | 40 |
| 🔍 Manual Testing | Entry → Lead | 40 |
| 🤖 Automation Engineering | Entry → Lead | 40 |
| 🔌 API Testing | Entry → Lead | 40 |
| ⚙️ CI / CD | Entry → Lead | 40 |
| 🏗️ System Design | Entry → Lead | 40 |
| 🔒 Security Testing | Mid → Lead | 30 |
| ⚡ Performance Testing | Entry → Lead | 40 |
| 📊 Data & AI Testing | Entry → Lead | 40 |
| 📚 QA Theory & Fundamentals | Entry → Senior | 30 |

**Total: 360 questions**

---

## Project structure

```
qa-encyclopedia/
├── _questions/          # One .md file per question (single source of truth)
├── behavioral/
├── manual-testing/
├── automation/
├── api-testing/
├── ci-cd/
├── system-design/
├── security-testing/
├── performance-testing/
├── data-ai-testing/
└── qa-theory/
```

Each category folder contains level pages (`entry.md`, `mid.md`, `senior.md`, `lead.md`) that list all questions for that level and link to the full question pages in `_questions/`.

---

## Run it locally

**Prerequisites:** Ruby 3.x, Bundler (`gem install bundler`)

```bash
git clone https://github.com/7eregaDo/qa-encyclopedia.git
cd qa-encyclopedia
bundle install
bundle exec jekyll serve
# Open http://localhost:4000/qa-encyclopedia
```

---

## Adding a question

1. Create `_questions/<category>/<level>/qXXX.md` using the template below
2. The question will appear automatically on the relevant level page

```yaml
---
question_id: 999
title: "Your question title here"
category: api-testing
level: senior
---

## The Intent
What the interviewer is testing for.

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
| **Lead** | ... |

## Key Terms
| Term | Definition |
|------|------------|
| **Term** | Definition here |
```

---

## License

MIT