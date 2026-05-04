---
layout: default
title: "CI / CD — Lead"
category: ci-cd
level: lead
---

# ⚙️ CI / CD

> CI/CD covers continuous integration, delivery, deployment, pipelines, quality gates, monitoring, and automation infrastructure.

---

**Level:** [Entry](/ci-cd/entry/) | [Mid](/ci-cd/mid/) | [Senior](/ci-cd/senior/) | **Lead**

<div class="level-description">
<em>Leadership questions for QA leads, managers, and heads of quality. Focus on org-wide impact, culture, vendor management, and executive communication.</em>
</div>

---

### 0 Questions at Lead level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
