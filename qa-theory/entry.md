---
layout: default
title: "QA Theory & Fundamentals — Entry"
category: qa-theory
level: entry
---

<div class="module-container">

# 📚 QA Theory & Fundamentals

> Testing pyramid, bug lifecycle, seven principles, V-model, TMMi, mutation testing, RCA, and exploratory testing philosophy.

---

<div class="level-nav-bar">
  <strong>Level:</strong> 
  <a href="/qa-theory/entry/" class="level-tab active">Entry</a> 
  <a href="/qa-theory/mid/" class="level-tab">Mid</a> 
  <a href="/qa-theory/senior/" class="level-tab">Senior</a> 
  <a href="/qa-theory/lead/" class="level-tab">Lead</a>
</div>

<div class="level-description">
  Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.
</div>

### Questions at Entry level

<div class="question-list-grid">
{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}
</div>

<hr style="opacity: 0.1; margin: 40px 0;">

<p style="font-size:0.85rem;">
  <a href="{{ site.baseurl }}/" style="color: #06b6d4; text-decoration: none;">← Back to Home</a>
</p>

</div>