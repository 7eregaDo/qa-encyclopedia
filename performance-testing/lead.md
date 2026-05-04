---
layout: default
title: "Performance Testing — Lead"
category: performance-testing
level: lead
---

# ⚡ Performance Testing

> Load, stress, soak, and chaos testing. Percentiles, connection pools, Redis hot keys, Kubernetes resiliency, and auto-scaling.

---

**Level:** [Entry](/performance-testing/entry/) | [Mid](/performance-testing/mid/) | [Senior](/performance-testing/senior/) | **Lead**

<div class="level-description">
<em>Leadership questions for QA leads, managers, and heads of quality. Focus on org-wide impact, culture, vendor management, and executive communication.</em>
</div>

---

### 5 Questions at Lead level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
