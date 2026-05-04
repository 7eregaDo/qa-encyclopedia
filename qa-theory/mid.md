---
layout: default
title: "QA Theory & Fundamentals — Mid"
category: qa-theory
level: mid
---

# 📚 QA Theory & Fundamentals

> Testing pyramid, bug lifecycle, seven principles, V-model, TMMi, mutation testing, RCA, and exploratory testing philosophy.

---

**Level:** [Entry](/qa-theory/entry/) | **Mid** | [Senior](/qa-theory/senior/)

<div class="level-description">
<em>Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.</em>
</div>

---

### 7 Questions at Mid level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
