---
layout: default
title: "QA Theory & Fundamentals — Senior"
category: qa-theory
level: senior
---

# 📚 QA Theory & Fundamentals

> Testing pyramid, bug lifecycle, seven principles, V-model, TMMi, mutation testing, RCA, and exploratory testing philosophy.

---

**Level:** [Entry](/qa-theory/entry/) | [Mid](/qa-theory/mid/) | **Senior**

<div class="level-description">
<em>Advanced questions for senior QAs with 5+ years of experience. Focus on strategy, architecture, trade-offs, and cross-team influence.</em>
</div>

---

### 5 Questions at Senior level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
