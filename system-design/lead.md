---
layout: default
title: "System Design — Lead"
category: system-design
level: lead
---

# 🏗️ System Design

> Microservices, distributed systems, caching, sharding, circuit breakers, CAP theorem, and scalability testing at 1M+ users.

---

**Level:** [Entry](/system-design/entry/) | [Mid](/system-design/mid/) | [Senior](/system-design/senior/) | **Lead**

<div class="level-description">
<em>Leadership questions for QA leads, managers, and heads of quality. Focus on org-wide impact, culture, vendor management, and executive communication.</em>
</div>

---

### 10 Questions at Lead level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
