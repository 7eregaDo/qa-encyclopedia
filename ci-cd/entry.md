---
layout: default
title: "CI / CD — Entry"
category: ci-cd
level: entry
---

# ⚙️ CI / CD

> Pipeline design, quality gates, deployment strategies (Blue/Green, Canary), database migrations, and shift-left practices.

---

**Level:** **Entry** | [Mid](/ci-cd/mid/) | [Senior](/ci-cd/senior/)

<div class="level-description">
<em>Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.</em>
</div>

---

### 3 Questions at Entry level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
