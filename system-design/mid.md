---
layout: default
title: "System Design — Mid"
category: system-design
level: mid
---

# 🏗️ System Design

> Microservices, distributed systems, caching, sharding, circuit breakers, CAP theorem, and scalability testing at 1M+ users.

---

**Level:** [Entry](/system-design/entry/) | **Mid** | [Senior](/system-design/senior/) | [Lead](/system-design/lead/)

<div class="level-description">
<em>Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.</em>
</div>

---

### 2 Questions at Mid level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
