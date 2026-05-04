---
layout: default
title: "Behavioural Testing — Lead"
category: behavioral
level: lead
---

# 🧠 Behavioural Testing

> Situational and leadership questions using the STAR framework. Tests conflict resolution, prioritisation, mentoring, and stakeholder management.

---

**Level:** [Entry](/behavioral/entry/) | [Mid](/behavioral/mid/) | [Senior](/behavioral/senior/) | **Lead**

<div class="level-description">
<em>Leadership questions for QA leads, managers, and heads of quality. Focus on org-wide impact, culture, vendor management, and executive communication.</em>
</div>

---

### 22 Questions at Lead level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
