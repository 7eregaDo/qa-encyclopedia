---
layout: default
title: "Data & AI Testing — Mid"
category: data-ai-testing
level: mid
---

# 📊 Data & AI Testing

> ETL pipelines, ML model bias, data partitioning, ACID properties, feature stores, streaming validation, and post-mortem culture.

---

**Level:** [Entry](/data-ai-testing/entry/) | **Mid** | [Senior](/data-ai-testing/senior/) | [Lead](/data-ai-testing/lead/)

<div class="level-description">
<em>Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.</em>
</div>

---

### 5 Questions at Mid level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
