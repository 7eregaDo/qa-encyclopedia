---
layout: default
title: "Performance Testing — Mid"
category: performance-testing
level: mid
---

# ⚡ Performance Testing

> Load, stress, soak, and chaos testing. Percentiles, connection pools, Redis hot keys, Kubernetes resiliency, and auto-scaling.

---

**Level:** [Entry](/performance-testing/entry/) | **Mid** | [Senior](/performance-testing/senior/) | [Lead](/performance-testing/lead/)

<div class="level-description">
<em>Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.</em>
</div>

---

### 4 Questions at Mid level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
