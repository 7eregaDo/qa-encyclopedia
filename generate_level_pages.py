#!/usr/bin/env python3
"""
Generates all category level pages (entry.md, mid.md, senior.md, lead.md)
from the master mapping. Run from qa-encyclopedia root:
  python3 generate_level_pages.py
"""

import os

# ── Master Mapping ─────────────────────────────────────────────────────────────
# Format: { "folder": { "level": [question_ids] } }

MAPPING = {
    "behavioral": {
        "entry":  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 145],
        "mid":    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 145, 292],
        "senior": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 292, 316],
        "lead":   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 294, 296, 315, 316, 766, 774, 775],
    },
    "manual-testing": {
        "entry":  [16, 17, 21, 25],
        "mid":    [16, 17, 19, 21, 23, 24, 25, 142, 143, 164, 166, 169, 171, 226],
        "senior": [19, 21, 23, 24, 143, 164, 167, 169, 295, 740, 756, 767, 774],
        "lead":   [786, 787, 788],
    },
    "automation": {
        "entry":  [41, 42, 43, 44, 783],
        "mid":    [45, 227, 428, 768, 769, 770, 772, 773],
        "senior": [170, 215, 216, 227, 352, 429, 446, 447, 748, 749, 750, 769, 771, 772],
        "lead":   [784, 785, 786],
    },
    "api-testing": {
        "entry":  [71, 72, 74, 75, 76],
        "mid":    [74, 75, 76, 77, 79, 126, 187, 759, 760],
        "senior": [188, 190, 349, 758, 759, 760, 761, 762, 777, 778, 779],
    },
    "ci-cd": {
        "entry":  [82, 84, 351],
        "mid":    [83, 87, 89, 257, 258, 351, 753],
        "senior": [86, 88, 258, 352, 447, 751, 752, 753, 775, 780],
    },
    "system-design": {
        "entry":  [350, 440],
        "mid":    [269, 440],
        "senior": [269, 349, 350, 745, 746, 747, 763, 764, 765, 776, 779, 782],
        "lead":   [350, 500, 745, 746, 747, 763, 765, 776, 779, 782],
    },
    "security-testing": {
        "mid":    [95, 112, 114, 117, 120, 781],
        "senior": [311, 313, 314, 757, 764, 778, 781],
        "lead":   [310, 312, 315, 316, 317, 318],
    },
    "performance-testing": {
        "entry":  [101, 261],
        "mid":    [103, 147, 430, 758],
        "senior": [105, 110, 174, 246, 337, 624, 625, 736, 747, 760, 763, 764, 765, 777, 778],
        "lead":   [405, 407, 747, 776, 782],
    },
    "data-ai-testing": {
        "entry":  [91, 92],
        "mid":    [199, 449, 450, 527, 528],
        "senior": [187, 188, 189, 190, 529, 530, 531, 664, 684],
        "lead":   [191, 657, 658, 659, 667],
    },
    "qa-theory": {
        "entry":  [16, 25, 790, 791, 792],
        "mid":    [94, 101, 126, 143, 164, 169, 170],
        "senior": [167, 298, 321, 754, 755],
    },
}

# ── Human-readable titles & descriptions per category ──────────────────────────
CATEGORY_META = {
    "behavioral": {
        "title": "Behavioural Testing",
        "icon": "🧠",
        "description": "Situational and leadership questions using the STAR framework. Tests conflict resolution, prioritisation, mentoring, and stakeholder management.",
    },
    "manual-testing": {
        "title": "Manual Testing",
        "icon": "🔍",
        "description": "Hands-on testing techniques — test design, bug reporting, exploratory charters, risk-based testing, and compliance audits.",
    },
    "automation": {
        "title": "Automation Engineering",
        "icon": "🤖",
        "description": "Framework design, locator strategy, parallel execution, flaky tests, CI integration, and scaling automation across teams.",
    },
    "api-testing": {
        "title": "API Testing",
        "icon": "🔌",
        "description": "REST, GraphQL, WebSockets, contract testing, authentication, idempotency, schema evolution, and gateway-level concerns.",
    },
    "ci-cd": {
        "title": "CI / CD",
        "icon": "⚙️",
        "description": "Pipeline design, quality gates, deployment strategies (Blue/Green, Canary), database migrations, and shift-left practices.",
    },
    "system-design": {
        "title": "System Design",
        "icon": "🏗️",
        "description": "Microservices, distributed systems, caching, sharding, circuit breakers, CAP theorem, and scalability testing at 1M+ users.",
    },
    "security-testing": {
        "title": "Security Testing",
        "icon": "🔒",
        "description": "OWASP Top 10, JWT vulnerabilities, CORS, rate limiting, penetration testing, SAST/DAST in CI, and compliance (GDPR/PCI-DSS).",
    },
    "performance-testing": {
        "title": "Performance Testing",
        "icon": "⚡",
        "description": "Load, stress, soak, and chaos testing. Percentiles, connection pools, Redis hot keys, Kubernetes resiliency, and auto-scaling.",
    },
    "data-ai-testing": {
        "title": "Data & AI Testing",
        "icon": "📊",
        "description": "ETL pipelines, ML model bias, data partitioning, ACID properties, feature stores, streaming validation, and post-mortem culture.",
    },
    "qa-theory": {
        "title": "QA Theory & Fundamentals",
        "icon": "📚",
        "description": "Testing pyramid, bug lifecycle, seven principles, V-model, TMMi, mutation testing, RCA, and exploratory testing philosophy.",
    },
}

LEVEL_ORDER = ["entry", "mid", "senior", "lead"]

LEVEL_DESCRIPTIONS = {
    "entry": "Foundational questions for QA engineers with 0–2 years of experience. Focus on core concepts, basic tool usage, and standard workflows.",
    "mid":   "Intermediate questions for QA engineers with 2–5 years of experience. Focus on ownership, tool proficiency, and end-to-end problem solving.",
    "senior": "Advanced questions for senior QAs with 5+ years of experience. Focus on strategy, architecture, trade-offs, and cross-team influence.",
    "lead":  "Leadership questions for QA leads, managers, and heads of quality. Focus on org-wide impact, culture, vendor management, and executive communication.",
}


def levels_for_category(category):
    return [l for l in LEVEL_ORDER if l in MAPPING[category]]


def make_level_page(category, level, question_ids):
    meta = CATEGORY_META[category]
    levels = levels_for_category(category)
    level_links = " | ".join(
        f"[{l.capitalize()}](../{l}/)" if l != level else f"**{l.capitalize()}**"
        for l in levels
    )
    question_count = len(question_ids)

    # Build question card includes
    cards = "\n".join(
        f"{{% include question_card.html id={qid} %}}"
        for qid in question_ids
    )

    return f"""---
layout: default
title: "{meta['title']} — {level.capitalize()}"
category: {category}
level: {level}
---

# {meta['icon']} {meta['title']}

> {meta['description']}

---

**Level:** {level_links}

<div class="level-description">
<em>{LEVEL_DESCRIPTIONS[level]}</em>
</div>

---

### {question_count} Question{"s" if question_count != 1 else ""} at {level.capitalize()} level

{cards}

---

<p style="font-size:0.85rem; color:#888;">
  <a href="{{{{ site.baseurl }}}}/">← Back to Home</a>
</p>
"""


# ── Generate all pages ─────────────────────────────────────────────────────────
created = 0
for category, levels in MAPPING.items():
    os.makedirs(category, exist_ok=True)
    for level, question_ids in levels.items():
        filepath = os.path.join(category, f"{level}.md")
        content = make_level_page(category, level, question_ids)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  ✅ {filepath}  ({len(question_ids)} questions)")
        created += 1

print(f"\n🎉 Generated {created} level pages across {len(MAPPING)} categories")
