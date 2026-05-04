---
layout: default
title: "API Testing — Entry"
category: api-testing
level: entry
---

# 🔌 API Testing

> REST, GraphQL, WebSockets, contract testing, authentication, idempotency, schema evolution, and gateway-level concerns.

---

**Level:** **Entry** | [Mid](/api-testing/mid/) | [Senior](/api-testing/senior/)

<div class="level-description">
<em>Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.</em>
</div>

---

### 5 Questions at Entry level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
