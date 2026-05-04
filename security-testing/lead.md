---
layout: default
title: "Security Testing — Lead"
category: security-testing
level: lead
---

# 🔒 Security Testing

> OWASP Top 10, JWT vulnerabilities, CORS, rate limiting, penetration testing, SAST/DAST in CI, and compliance (GDPR/PCI-DSS).

---

**Level:** [Mid](/security-testing/mid/) | [Senior](/security-testing/senior/) | **Lead**

<div class="level-description">
<em>Leadership questions for QA leads, managers, and heads of quality. Focus on org-wide impact, culture, vendor management, and executive communication.</em>
</div>

---

### 6 Questions at Lead level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
