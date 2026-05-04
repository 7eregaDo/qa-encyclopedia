---
layout: default
title: "Data & AI Testing — Senior"
category: data-ai-testing
level: senior
---

# 📊 Data & AI Testing

> ETL pipelines, ML model bias, data partitioning, ACID properties, feature stores, streaming validation, and post-mortem culture.

---

**Level:** [Entry](/data-ai-testing/entry/) | [Mid](/data-ai-testing/mid/) | **Senior** | [Lead](/data-ai-testing/lead/)

<div class="level-description">
<em>Advanced questions for senior QAs with 5+ years of experience. Focus on strategy, architecture, trade-offs, and cross-team influence.</em>
</div>

---

### 9 Questions at Senior level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
