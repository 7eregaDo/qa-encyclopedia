---
layout: default
title: "Automation Engineering — Lead"
category: automation
level: lead
---

# 🤖 Automation Engineering

> Framework design, locator strategy, parallel execution, flaky tests, CI integration, and scaling automation across teams.

---

**Level:** [Entry](/automation/entry/) | [Mid](/automation/mid/) | [Senior](/automation/senior/) | **Lead**

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
