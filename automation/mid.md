---
layout: default
title: "Automation Engineering — Mid"
category: automation
level: mid
---

# 🤖 Automation Engineering

> Framework design, locator strategy, parallel execution, flaky tests, CI integration, and scaling automation across teams.

---

**Level:** [Entry](/automation/entry/) | **Mid** | [Senior](/automation/senior/) | [Lead](/automation/lead/)

<div class="level-description">
<em>Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.</em>
</div>

---

### 8 Questions at Mid level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
