#!/usr/bin/env python3
"""
Generates index.md for each category folder.
Run from qa-encyclopedia root: python3 generate_category_indexes.py
"""

import os

CATEGORY_META = {
    "behavioral": {
        "title": "Behavioural Testing",
        "icon": "🧠",
        "description": "Situational and leadership questions using the STAR framework. Tests conflict resolution, prioritisation, mentoring, and stakeholder management.",
        "levels": ["entry", "mid", "senior", "lead"],
    },
    "manual-testing": {
        "title": "Manual Testing",
        "icon": "🔍",
        "description": "Hands-on testing techniques — test design, bug reporting, exploratory charters, risk-based testing, and compliance audits.",
        "levels": ["entry", "mid", "senior", "lead"],
    },
    "automation": {
        "title": "Automation Engineering",
        "icon": "🤖",
        "description": "Framework design, locator strategy, parallel execution, flaky tests, CI integration, and scaling automation across teams.",
        "levels": ["entry", "mid", "senior", "lead"],
    },
    "api-testing": {
        "title": "API Testing",
        "icon": "🔌",
        "description": "REST, GraphQL, WebSockets, contract testing, authentication, idempotency, schema evolution, and gateway-level concerns.",
        "levels": ["entry", "mid", "senior"],
    },
    "ci-cd": {
        "title": "CI / CD",
        "icon": "⚙️",
        "description": "Pipeline design, quality gates, deployment strategies (Blue/Green, Canary), database migrations, and shift-left practices.",
        "levels": ["entry", "mid", "senior"],
    },
    "system-design": {
        "title": "System Design",
        "icon": "🏗️",
        "description": "Microservices, distributed systems, caching, sharding, circuit breakers, CAP theorem, and scalability testing at 1M+ users.",
        "levels": ["entry", "mid", "senior", "lead"],
    },
    "security-testing": {
        "title": "Security Testing",
        "icon": "🔒",
        "description": "OWASP Top 10, JWT vulnerabilities, CORS, rate limiting, penetration testing, SAST/DAST in CI, and compliance (GDPR/PCI-DSS).",
        "levels": ["mid", "senior", "lead"],
    },
    "performance-testing": {
        "title": "Performance Testing",
        "icon": "⚡",
        "description": "Load, stress, soak, and chaos testing. Percentiles, connection pools, Redis hot keys, Kubernetes resiliency, and auto-scaling.",
        "levels": ["entry", "mid", "senior", "lead"],
    },
    "data-ai-testing": {
        "title": "Data & AI Testing",
        "icon": "📊",
        "description": "ETL pipelines, ML model bias, data partitioning, ACID properties, feature stores, streaming validation, and post-mortem culture.",
        "levels": ["entry", "mid", "senior", "lead"],
    },
    "qa-theory": {
        "title": "QA Theory & Fundamentals",
        "icon": "📚",
        "description": "Testing pyramid, bug lifecycle, seven principles, V-model, TMMi, mutation testing, RCA, and exploratory testing philosophy.",
        "levels": ["entry", "mid", "senior"],
    },
}

QUESTION_COUNTS = {
    "behavioral":        {"entry": 11, "mid": 13, "senior": 17, "lead": 22},
    "manual-testing":    {"entry": 4,  "mid": 14, "senior": 13, "lead": 3},
    "automation":        {"entry": 5,  "mid": 8,  "senior": 14, "lead": 3},
    "api-testing":       {"entry": 5,  "mid": 9,  "senior": 11},
    "ci-cd":             {"entry": 3,  "mid": 7,  "senior": 10},
    "system-design":     {"entry": 2,  "mid": 2,  "senior": 12, "lead": 10},
    "security-testing":  {"mid": 6,    "senior": 7, "lead": 6},
    "performance-testing":{"entry": 2, "mid": 4,  "senior": 15, "lead": 5},
    "data-ai-testing":   {"entry": 2,  "mid": 5,  "senior": 9,  "lead": 5},
    "qa-theory":         {"entry": 5,  "mid": 7,  "senior": 5},
}

for category, meta in CATEGORY_META.items():
    level_rows = ""
    total = 0
    for level in meta["levels"]:
        count = QUESTION_COUNTS[category].get(level, 0)
        total += count
        level_rows += f"| [{level.capitalize()}](./{level}/) | {count} questions | Foundational concepts and patterns for {level}-level QA engineers |\n"

    content = f"""---
layout: default
title: "{meta['title']}"
---

# {meta['icon']} {meta['title']}

> {meta['description']}

---

### Choose your level

| Level | Questions | Focus |
|-------|-----------|-------|
{level_rows}
**Total: {total} questions in this category**

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{{{ site.baseurl }}}}/">← Back to Home</a>
</p>
"""
    filepath = os.path.join(category, "index.md")
    with open(filepath, "w") as f:
        f.write(content)
    print(f"  ✅ {filepath}")

print(f"\n🎉 Generated {len(CATEGORY_META)} category index pages")
