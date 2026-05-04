---
layout: default
title: "Security Testing — Mid"
category: security-testing
level: mid
---

# 🔒 Security Testing

> OWASP Top 10, JWT vulnerabilities, CORS, rate limiting, penetration testing, SAST/DAST in CI, and compliance (GDPR/PCI-DSS).

---

**Level:** **Mid** | [Senior](/security-testing/senior/) | [Lead](/security-testing/lead/)

<div class="level-description">
<em>Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.</em>
</div>

---

### 6 Questions at Mid level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
