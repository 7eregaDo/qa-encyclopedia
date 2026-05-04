---
layout: default
title: "Manual Testing — Senior"
category: manual-testing
level: senior
---

# 🔍 Manual Testing

> Hands-on testing techniques — test design, bug reporting, exploratory charters, risk-based testing, and compliance audits.

---

**Level:** [Entry](/manual-testing/entry/) | [Mid](/manual-testing/mid/) | **Senior** | [Lead](/manual-testing/lead/)

<div class="level-description">
<em>Advanced questions for senior QAs with 5+ years of experience. Focus on strategy, architecture, trade-offs, and cross-team influence.</em>
</div>

---

### 13 Questions at Senior level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
