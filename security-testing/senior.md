---
layout: default
title: "Security Testing — Senior"
category: security-testing
level: senior
---

# 🔒 Security Testing

> OWASP Top 10, JWT vulnerabilities, CORS, rate limiting, penetration testing, SAST/DAST in CI, and compliance (GDPR/PCI-DSS).

---

**Level:** [Mid](/security-testing/mid/) | **Senior** | [Lead](/security-testing/lead/)

<div class="level-description">
<em>Advanced questions for senior QAs with 5+ years of experience. Focus on strategy, architecture, trade-offs, and cross-team influence.</em>
</div>

---

### 7 Questions at Senior level

{% assign filtered_questions = site.questions | where: "category", page.category | where: "level", page.level | sort: "question_id" %}

{% for q in filtered_questions %}
  {% include question_card.html id=q.question_id %}
{% endfor %}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
</p>
