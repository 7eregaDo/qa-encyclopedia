---
layout: default
title: "Automation Engineering — Entry"
category: automation
level: entry
---

# 🤖 Automation Engineering

> Framework design, locator strategy, parallel execution, flaky tests, CI integration, and scaling automation across teams.

---

**Level:** **Entry** | [Mid](/automation/mid/) | [Senior](/automation/senior/) | [Lead](/automation/lead/)

<div class="level-description">
<em>Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.</em>
</div>

---

### 5 Questions at Entry level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
