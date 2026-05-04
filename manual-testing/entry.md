---
layout: default
title: "Manual Testing — Entry"
category: manual-testing
level: entry
---

# 🔍 Manual Testing

> Hands-on testing techniques — test design, bug reporting, exploratory charters, risk-based testing, and compliance audits.

---

**Level:** **Entry** | [Mid](/manual-testing/mid/) | [Senior](/manual-testing/senior/) | [Lead](/manual-testing/lead/)

<div class="level-description">
<em>Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.</em>
</div>

---

### 4 Questions at Entry level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
