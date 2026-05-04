---
layout: default
title: "Security Testing — Entry"
category: security-testing
level: entry
---

# 🔒 Security Testing

> Security testing covers vulnerability discovery, threat modeling, authentication, encryption, injection attacks, and compliance.

---

**Level:** **Entry** | [Mid](/security-testing/mid/) | [Senior](/security-testing/senior/) | [Lead](/security-testing/lead/)

<div class="level-description">
<em>Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.</em>
</div>

---

### Questions at Entry level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
