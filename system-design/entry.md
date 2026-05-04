---
layout: default
title: "System Design — Entry"
category: system-design
level: entry
---

# 🏗️ System Design

> Microservices, distributed systems, caching, sharding, circuit breakers, CAP theorem, and scalability testing at 1M+ users.

---

**Level:** **Entry** | [Mid](/system-design/mid/) | [Senior](/system-design/senior/) | [Lead](/system-design/lead/)

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
