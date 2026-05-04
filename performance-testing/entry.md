---
layout: default
title: "Performance Testing — Entry"
category: performance-testing
level: entry
---

# ⚡ Performance Testing

> Load, stress, soak, and chaos testing. Percentiles, connection pools, Redis hot keys, Kubernetes resiliency, and auto-scaling.

---

**Level:** **Entry** | [Mid](/performance-testing/mid/) | [Senior](/performance-testing/senior/) | [Lead](/performance-testing/lead/)

<div class="level-description">
<em>Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.</em>
</div>

---

### 2 Questions at Entry level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
