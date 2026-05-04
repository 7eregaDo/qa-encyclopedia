---
layout: default
title: "Manual Testing — Mid"
category: manual-testing
level: mid
---

# 🔍 Manual Testing

> Hands-on testing techniques — test design, bug reporting, exploratory charters, risk-based testing, and compliance audits.

---

**Level:** [Entry](/manual-testing/entry/) | **Mid** | [Senior](/manual-testing/senior/) | [Lead](/manual-testing/lead/)

<div class="level-description">
<em>Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.</em>
</div>

---

### 14 Questions at Mid level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
