---
layout: default
title: "Behavioural Testing"
category: behavioral
level: entry
---

# 🧠 Behavioural Testing

> Situational and leadership questions using the STAR framework. Tests conflict resolution, prioritisation, mentoring, and stakeholder management.

---

**Level:** **Entry** | [Mid](/behavioral/mid/) | [Senior](/behavioral/senior/) | [Lead](/behavioral/lead/)

<div class="level-description">
<em>Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.</em>
</div>

---

### Questions at Entry level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

<hr>

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>