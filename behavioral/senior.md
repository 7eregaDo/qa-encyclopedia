---
layout: default
title: "Behavioural Testing — Senior"
category: behavioral
level: senior
---

... header info ...

### Questions at Entry level

{% comment %} Filter collection by category AND level, then sort by ID {% endcomment %}
{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}