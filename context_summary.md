# Project Context: QA Encyclopedia

## 1. Technical Stack & Architecture
- **Framework:** Jekyll (Static Site Generator)[cite: 1].
- **Data Model:** Jekyll Collections[cite: 1].
- **Collection Name:** `_questions`[cite: 1].
- **Directory Structure:** `_questions/{category}/{level}/q{id}.md`[cite: 1].
- **Configuration:** `_config.yml` must have `collections.questions.output: true`[cite: 1].

## 2. Content Standards ("Claude Style")
Every question is a standalone Markdown file designed for a specific seniority level[cite: 1].
- **Front Matter Requirements:**
  - `question_id`: (Integer)[cite: 1]
  - `title`: (String) The specific interview question[cite: 1].
  - `category`: (String)[cite: 1]
  - `level`: (String)[cite: 1]
  - `theory`: (String) A brief, formal definition of the concept[cite: 1].
- **Body Structure:**
  - **The Intent:** Why the interviewer is asking this[cite: 1].
  - **The STAR Script:** A concrete Situation, Task, Action, and Result[cite: 1].
  - **Seniority Shift:** Explaining how depth changes across levels[cite: 1].
  - **Key Terms/Quick Reference:** Tables or bulleted definitions[cite: 1].

## 3. Implementation Details
- **Filtering Logic:** Level pages (e.g., `automation/senior.md`) use Liquid to filter the collection: 
  `site.questions | where: "category", "automation" | where: "level", "senior"`[cite: 1].
- **Dynamic Cards:** `_includes/question_card.html` renders the content using the `question_id` passed as a parameter[cite: 1].

## 4. Modules to be covered
1. qa-theory/
2. behavioral/
3. manual-testing/
4. automation/
5. api-testing/
6. ci-cd/
7. system-design/
8. security-testing/
9. performance-testing/
10. data-ai-testing/