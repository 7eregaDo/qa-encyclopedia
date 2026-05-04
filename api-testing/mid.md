---
layout: default
title: "API Testing — Mid"
category: api-testing
level: mid
---

# 🔌 API Testing

> REST, GraphQL, WebSockets, contract testing, authentication, idempotency, schema evolution, and gateway-level concerns.

---

**Level:** [Entry](/api-testing/entry/) | **Mid** | [Senior](/api-testing/senior/)

<div class="level-description">
<em>Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.</em>
</div>

---

### 9 Questions at Mid level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
