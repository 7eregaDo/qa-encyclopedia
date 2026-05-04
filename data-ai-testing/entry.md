---
layout: default
title: "Data & AI Testing — Entry"
category: data-ai-testing
level: entry
---

# 📊 Data & AI Testing

> ETL pipelines, ML model bias, data partitioning, ACID properties, feature stores, streaming validation, and post-mortem culture.

---

**Level:** **Entry** | [Mid](/data-ai-testing/mid/) | [Senior](/data-ai-testing/senior/) | [Lead](/data-ai-testing/lead/)

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
