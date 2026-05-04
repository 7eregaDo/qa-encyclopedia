---
layout: default
title: "Automation Engineering — Senior"
category: automation
level: senior
---

# 🤖 Automation Engineering

> Framework design, locator strategy, parallel execution, flaky tests, CI integration, and scaling automation across teams.

---

**Level:** [Entry](/automation/entry/) | [Mid](/automation/mid/) | **Senior** | [Lead](/automation/lead/)

<div class="level-description">
<em>Advanced questions for senior QAs with 5+ years of experience. Focus on strategy, architecture, trade-offs, and cross-team influence.</em>
</div>

---

### 14 Questions at Senior level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
