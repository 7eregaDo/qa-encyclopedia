# QA Encyclopedia

A public knowledge base of QA interview questions, structured by category and seniority level.

## 🚀 Live Site
[yourusername.github.io/qa-encyclopedia](https://yourusername.github.io/qa-encyclopedia)

---

## 📁 Structure

```
qa-encyclopedia/
├── _questions/          # One .md file per question (single source of truth)
├── behavioral/          # entry, mid, senior, lead
├── manual-testing/      # entry, mid, senior, lead
├── automation/          # entry, mid, senior, lead
├── api-testing/         # entry, mid, senior
├── ci-cd/               # entry, mid, senior
├── system-design/       # entry, mid, senior, lead
├── security-testing/    # mid, senior, lead
├── performance-testing/ # entry, mid, senior, lead
├── data-ai-testing/     # entry, mid, senior, lead
└── qa-theory/           # entry, mid, senior
```

Each level page (e.g. `automation/senior.md`) lists all questions for that level with links to the full question page in `_questions/`.

---

## 🛠️ Local Setup

### Prerequisites
- Ruby 3.x
- Bundler (`gem install bundler`)

### Run locally
```bash
git clone https://github.com/yourusername/qa-encyclopedia.git
cd qa-encyclopedia
bundle install
bundle exec jekyll serve
# Open http://localhost:4000/qa-encyclopedia
```

---

## 🌐 GitHub Pages Deployment

1. Push this repo to GitHub as `qa-encyclopedia`
2. Go to **Settings → Pages**
3. Set source to **Deploy from branch → main → / (root)**
4. Wait ~2 minutes — your site will be live at `https://yourusername.github.io/qa-encyclopedia`

> **Important:** Update `url` and `baseurl` in `_config.yml` with your actual GitHub username before deploying.

---

## ✍️ Adding a New Question

1. Create `_questions/qXXX.md` using the template below
2. Add the question number to the relevant level pages

### Question template
```yaml
---
id: 999
title: "Your question title here"
category: automation
levels: [entry, mid]
theory: false
source: new   # use 'pdf' for original questions, 'new' for chat additions
---

## Intent
What this question is testing.

## Answer (STAR)

**Situation:** ...

**Task:** ...

**Action:** ...

**Result:** ...

## Seniority Shift
- **Entry/Mid:** Focus on...
- **Senior/Lead:** Focus on...
```

---

## 📊 Question Register

| Range | Topic |
|-------|-------|
| 1–15 | Behavioral Leadership & Conflict |
| 16–100 | Manual Testing & SQL Fundamentals |
| 101–200 | Performance, Accessibility & Mobile |
| 201–350 | Automation, CI/CD & Cloud |
| 351–500 | System Design & Architecture |
| 501–744 | Data, AI & Regulated Software |
| 745–792 | Strategic Architecture (New) |

---

## 🤝 Contributing

PRs welcome. Please follow the question template and map your question to the correct level files.

---

## 📄 License

MIT
