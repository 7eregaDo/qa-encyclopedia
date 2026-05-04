---
layout: default
title: "CI / CD — Senior"
category: ci-cd
level: senior
---

# ⚙️ CI / CD

> Pipeline design, quality gates, deployment strategies (Blue/Green, Canary), database migrations, and shift-left practices.

---

**Level:** [Entry](/ci-cd/entry/) | [Mid](/ci-cd/mid/) | **Senior**

<div class="level-description">
<em>Advanced questions for senior QAs with 5+ years of experience. Focus on strategy, architecture, trade-offs, and cross-team influence.</em>
</div>

---

### 10 Questions at Senior level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
