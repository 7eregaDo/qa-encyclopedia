---
layout: default
title: "Manual Testing — Lead"
category: manual-testing
level: lead
---

# 🔍 Manual Testing

> Hands-on testing techniques — test design, bug reporting, exploratory charters, risk-based testing, and compliance audits.

---

**Level:** [Entry](/manual-testing/entry/) | [Mid](/manual-testing/mid/) | [Senior](/manual-testing/senior/) | **Lead**

<div class="level-description">
<em>Leadership questions for QA leads, managers, and heads of quality. Focus on org-wide impact, culture, vendor management, and executive communication.</em>
</div>

---

### 3 Questions at Lead level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
