---
layout: default
title: "API Testing — Senior"
category: api-testing
level: senior
---

# 🔌 API Testing

> REST, GraphQL, WebSockets, contract testing, authentication, idempotency, schema evolution, and gateway-level concerns.

---

**Level:** [Entry](/api-testing/entry/) | [Mid](/api-testing/mid/) | **Senior**

<div class="level-description">
<em>Advanced questions for senior QAs with 5+ years of experience. Focus on strategy, architecture, trade-offs, and cross-team influence.</em>
</div>

---

### 11 Questions at Senior level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
