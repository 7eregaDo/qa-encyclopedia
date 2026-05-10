# QA Encyclopedia Task Instructions (STRICT EXECUTION)

I am continuing a QA Encyclopedia project.

You will receive:

* A context summary (source of truth)
* Two markdown files containing interview questions

---

## Your Tasks (STRICT EXECUTION)

### 1. Understand Context

* Read and fully follow the provided context summary
* Do NOT deviate from structure or rules

---

### 2. Normalize & Analyze Questions

For EACH question:

* Identify its **core concept**
* Determine ALL applicable seniority levels:

  * entry
  * mid
  * senior
  * lead

A question MAY belong to multiple levels

---

### 3. Regenerate Questions Per Level (CRITICAL)

For EACH applicable level:

* Rewrite the question **completely**
* Adjust depth according to seniority rules

**DO NOT:**

* reuse the same wording
* only slightly tweak phrasing

**DO:**

* change scope, complexity, and intent

---

### 4. Output Format (MANDATORY)

For each generated question:

* Produce a **FULL markdown file**
* Follow EXACT structure from context

---

### 5. Categorization

* Assign category based on concept (e.g., automation, performance, API, etc.)

Ensure correct folder mapping:

```id="w2xqf3"
_questions/{category}/{level}/q{id}.md
```

---

### 6. ID Rules

* Ensure each question has a **UNIQUE question_id**
* IDs must NOT collide with existing ones

---

### 7. Output Constraints

* No explanations outside markdown files
* No summaries
* No commentary
* ONLY final files

---

### 8. Quality Enforcement

* If a question is too shallow for a level:

  * **EXPAND it**

* If too complex:

  * **SIMPLIFY it**

Each level must feel:

* natural
* realistic for interviews
* aligned with industry expectations
