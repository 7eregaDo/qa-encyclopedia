#!/usr/bin/env python3
"""
Generates all _questions/qXXX.md stub files from the master mapping.
Run from the qa-encyclopedia root: python3 generate_stubs.py
"""

import os

OUTPUT_DIR = "_questions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Master question registry ──────────────────────────────────────────────────
# Format: id -> { title, category, levels, theory, source }
# source: "pdf" = original book | "new" = added in session

QUESTIONS = {
    # ── BEHAVIORAL (1-15, 145, 292, 294, 296, 315, 316) ───────────────────
    1:  {"title": "Tell me about a time you disagreed with a developer over a bug priority.", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    2:  {"title": "Describe a situation where you had to meet an impossible deadline.", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    3:  {"title": "Tell me about a time you caught a critical bug late in the cycle.", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    4:  {"title": "How do you handle being pressured to sign off on untested code?", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    5:  {"title": "Describe a time you had to learn a new tool or technology quickly.", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    6:  {"title": "Tell me about a time you improved a QA process.", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    7:  {"title": "Describe a conflict with a product manager about scope.", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    8:  {"title": "Tell me about a time you mentored a junior team member.", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    9:  {"title": "How do you prioritize when you have more bugs than time?", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    10: {"title": "Describe a project where you had to work with incomplete requirements.", "category": "behavioral", "levels": ["entry","mid","senior","lead"], "theory": False, "source": "pdf"},
    11: {"title": "Tell me about a time you failed and what you learned.", "category": "behavioral", "levels": ["mid","senior","lead"], "theory": False, "source": "pdf"},
    12: {"title": "How do you build trust with a new engineering team?", "category": "behavioral", "levels": ["senior","lead"], "theory": False, "source": "pdf"},
    13: {"title": "Describe a time you drove a quality initiative from scratch.", "category": "behavioral", "levels": ["senior","lead"], "theory": False, "source": "pdf"},
    14: {"title": "How do you influence without authority?", "category": "behavioral", "levels": ["senior","lead"], "theory": False, "source": "pdf"},
    15: {"title": "Tell me about a time you had to make a high-risk release decision.", "category": "behavioral", "levels": ["senior","lead"], "theory": False, "source": "pdf"},
    145: {"title": "How do you stay up to date with QA tools and practices?", "category": "behavioral", "levels": ["entry","mid"], "theory": False, "source": "pdf"},
    292: {"title": "Tell me about a time you advocated for quality when it wasn't popular.", "category": "behavioral", "levels": ["mid","senior"], "theory": False, "source": "pdf"},
    294: {"title": "How do you handle a team that sees QA as a bottleneck?", "category": "behavioral", "levels": ["lead"], "theory": False, "source": "pdf"},
    296: {"title": "Describe how you built a QA culture from scratch.", "category": "behavioral", "levels": ["lead"], "theory": False, "source": "pdf"},
    315: {"title": "Security Leadership and Policy: How do you set org-wide security standards?", "category": "behavioral", "levels": ["lead"], "theory": False, "source": "new"},
    316: {"title": "How do you manage stakeholder pressure when a deadline conflicts with quality?", "category": "behavioral", "levels": ["senior","lead"], "theory": False, "source": "pdf"},

    # ── MANUAL TESTING ─────────────────────────────────────────────────────
    16: {"title": "What is the difference between Verification and Validation?", "category": "manual-testing", "levels": ["entry","mid"], "theory": True, "source": "pdf"},
    17: {"title": "What is a Test Plan and what does it contain?", "category": "manual-testing", "levels": ["entry","mid"], "theory": False, "source": "pdf"},
    19: {"title": "What are the key differences between Web and Mobile testing?", "category": "manual-testing", "levels": ["mid","senior"], "theory": False, "source": "new"},
    21: {"title": "Explain Boundary Value Analysis (BVA) and Equivalence Partitioning (EP).", "category": "manual-testing", "levels": ["entry","mid","senior"], "theory": True, "source": "pdf"},
    23: {"title": "What is Exploratory Testing and when do you use it?", "category": "manual-testing", "levels": ["mid","senior"], "theory": False, "source": "pdf"},
    24: {"title": "How do you write a good bug report?", "category": "manual-testing", "levels": ["mid","senior"], "theory": False, "source": "pdf"},
    25: {"title": "What is Regression Testing vs. Re-testing?", "category": "manual-testing", "levels": ["entry","mid"], "theory": True, "source": "pdf"},
    143: {"title": "What is a 'Definition of Done' and how do you enforce it?", "category": "manual-testing", "levels": ["mid","senior"], "theory": False, "source": "pdf"},
    142: {"title": "Definition of Done (DoD) in Testing.", "category": "manual-testing", "levels": ["mid"], "theory": False, "source": "new"},
    164: {"title": "What is State Transition Testing?", "category": "manual-testing", "levels": ["mid","senior"], "theory": True, "source": "pdf"},
    166: {"title": "What is Decision Table Testing?", "category": "manual-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    167: {"title": "What is Pairwise (All-Pairs) Testing?", "category": "manual-testing", "levels": ["senior"], "theory": True, "source": "pdf"},
    169: {"title": "How do you design an Exploratory Testing charter?", "category": "manual-testing", "levels": ["mid","senior"], "theory": True, "source": "pdf"},
    171: {"title": "What is the difference between a Test Strategy and a Test Plan?", "category": "manual-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    226: {"title": "How do you test a feature with no requirements?", "category": "manual-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    295: {"title": "How do you test a Legacy system with no documentation?", "category": "manual-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    740: {"title": "How do you test for Time-Bomb bugs (e.g. Leap Year / Year 2038)?", "category": "manual-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    756: {"title": "How do you implement Risk-Based Testing (RBT) to optimise a 5,000-test suite?", "category": "manual-testing", "levels": ["senior"], "theory": False, "source": "new"},
    767: {"title": "How do you audit a site for WCAG 2.1 Compliance using a Screen Reader?", "category": "manual-testing", "levels": ["senior"], "theory": False, "source": "new"},
    774: {"title": "How do you perform a Root Cause Analysis (RCA) on a major Production Leak?", "category": "manual-testing", "levels": ["senior","lead"], "theory": False, "source": "new"},
    786: {"title": "How do you design a Master Test Strategy for a multi-year enterprise project?", "category": "manual-testing", "levels": ["lead"], "theory": False, "source": "new"},
    787: {"title": "How do you manage an outsourced/offshore QA vendor effectively?", "category": "manual-testing", "levels": ["lead"], "theory": False, "source": "new"},
    788: {"title": "How do you lead a team through a SOC2 or ISO 27001 Quality Audit?", "category": "manual-testing", "levels": ["lead"], "theory": False, "source": "new"},

    # ── AUTOMATION ─────────────────────────────────────────────────────────
    41: {"title": "What is the Page Object Model (POM) and why do we use it?", "category": "automation", "levels": ["entry"], "theory": False, "source": "pdf"},
    42: {"title": "What are Flaky Tests and how do you identify them?", "category": "automation", "levels": ["entry"], "theory": False, "source": "pdf"},
    43: {"title": "What is the difference between Implicit and Explicit Waits?", "category": "automation", "levels": ["entry"], "theory": False, "source": "pdf"},
    44: {"title": "How do you choose the best Locator (ID, CSS, XPath) for an element?", "category": "automation", "levels": ["entry"], "theory": False, "source": "pdf"},
    45: {"title": "What is Data-Driven Testing (DDT) and how have you implemented it?", "category": "automation", "levels": ["mid"], "theory": False, "source": "pdf"},
    170: {"title": "What is Mutation Testing and when would you use it?", "category": "automation", "levels": ["senior"], "theory": True, "source": "pdf"},
    215: {"title": "How do you design a framework for parallel cross-browser execution?", "category": "automation", "levels": ["senior"], "theory": False, "source": "pdf"},
    216: {"title": "How do you integrate your automation suite with a CI/CD pipeline?", "category": "automation", "levels": ["senior"], "theory": False, "source": "pdf"},
    227: {"title": "What is Contract Testing and how does it differ from E2E testing?", "category": "automation", "levels": ["mid","senior"], "theory": False, "source": "pdf"},
    352: {"title": "How do you manage test data at scale in an automation framework?", "category": "automation", "levels": ["senior"], "theory": False, "source": "pdf"},
    428: {"title": "How do you handle dynamic elements and Shadow DOM in Playwright/Selenium?", "category": "automation", "levels": ["mid"], "theory": False, "source": "pdf"},
    429: {"title": "How do you implement visual regression testing?", "category": "automation", "levels": ["senior"], "theory": False, "source": "pdf"},
    446: {"title": "How do you test a micro-frontend architecture?", "category": "automation", "levels": ["senior"], "theory": False, "source": "pdf"},
    447: {"title": "How do you enforce coding standards in a large automation repo?", "category": "automation", "levels": ["senior"], "theory": False, "source": "pdf"},
    748: {"title": "How do you build a custom DSL (Domain Specific Language) for a test framework?", "category": "automation", "levels": ["senior"], "theory": False, "source": "new"},
    749: {"title": "How do you manage Dependency Hell and versioning in a massive automation repo?", "category": "automation", "levels": ["senior"], "theory": False, "source": "new"},
    750: {"title": "What is your strategy for Parallel Execution across Grid vs Cloud?", "category": "automation", "levels": ["senior"], "theory": False, "source": "new"},
    768: {"title": "Why are Implicit Waits considered bad practice and what is your alternative?", "category": "automation", "levels": ["mid"], "theory": False, "source": "new"},
    769: {"title": "How do you use API-First setup to speed up UI tests?", "category": "automation", "levels": ["mid","senior"], "theory": False, "source": "new"},
    770: {"title": "How do you test React/Vue Components in isolation?", "category": "automation", "levels": ["mid"], "theory": False, "source": "new"},
    771: {"title": "Page Object Model (POM) vs Screenplay Pattern: which do you choose and why?", "category": "automation", "levels": ["senior"], "theory": False, "source": "new"},
    772: {"title": "How do you handle Flaky Tests in a large CI/CD pipeline?", "category": "automation", "levels": ["mid","senior"], "theory": False, "source": "new"},
    773: {"title": "How do you implement Data-Driven Testing (DDT) using external sources?", "category": "automation", "levels": ["mid"], "theory": False, "source": "new"},
    783: {"title": "What is the difference between an Assertion and a Verification?", "category": "automation", "levels": ["entry"], "theory": False, "source": "new"},
    784: {"title": "How do you decide between building a custom framework vs a low-code tool?", "category": "automation", "levels": ["lead"], "theory": False, "source": "new"},
    785: {"title": "How do you define and report Automation ROI to non-technical stakeholders?", "category": "automation", "levels": ["lead"], "theory": False, "source": "new"},
    786: {"title": "How do you scale automation across 10+ autonomous squads without 10 frameworks?", "category": "automation", "levels": ["lead"], "theory": False, "source": "new"},

    # ── API TESTING ────────────────────────────────────────────────────────
    71: {"title": "What is a REST API and what are the main HTTP methods?", "category": "api-testing", "levels": ["entry"], "theory": True, "source": "pdf"},
    72: {"title": "What is the difference between PUT and PATCH?", "category": "api-testing", "levels": ["entry"], "theory": True, "source": "pdf"},
    74: {"title": "What is the difference between SOAP and REST?", "category": "api-testing", "levels": ["entry","mid"], "theory": True, "source": "pdf"},
    75: {"title": "How do you test API Authentication (Bearer Tokens vs API Keys)?", "category": "api-testing", "levels": ["entry","mid"], "theory": False, "source": "pdf"},
    76: {"title": "What is Negative Testing for an API?", "category": "api-testing", "levels": ["entry","mid"], "theory": False, "source": "pdf"},
    77: {"title": "What is Contract Testing and how does Pact work?", "category": "api-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    79: {"title": "How do you validate a JSON Schema in API testing?", "category": "api-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    126: {"title": "How do you use a Screen Reader (NVDA/VoiceOver) for accessibility testing?", "category": "api-testing", "levels": ["mid"], "theory": True, "source": "pdf"},
    187: {"title": "How do you test an ETL pipeline for data accuracy?", "category": "api-testing", "levels": ["mid","senior"], "theory": False, "source": "pdf"},
    188: {"title": "How do you validate data transformation logic in a pipeline?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    190: {"title": "How do you test for data loss in a streaming pipeline?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    349: {"title": "How do you design an API testing strategy for a microservices architecture?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    758: {"title": "What is the difference between a Stress Test and a Soak Test for a high-traffic API?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "new"},
    759: {"title": "How do you test Idempotency in a Payment API?", "category": "api-testing", "levels": ["mid","senior"], "theory": False, "source": "new"},
    760: {"title": "How do you test GraphQL Resolvers for Over-fetching and N+1 issues?", "category": "api-testing", "levels": ["mid","senior"], "theory": False, "source": "new"},
    761: {"title": "How do you test API Versioning to prevent breaking public-facing clients?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "new"},
    762: {"title": "Contract Testing: what happens when the Provider breaks the contract?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "new"},
    777: {"title": "How do you test WebSockets and Real-Time APIs (e.g. Chat or Stock Tickers)?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "new"},
    778: {"title": "How do you test Rate Limiting at the API Gateway level?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "new"},
    779: {"title": "How do you validate Event Schema Evolution in an Event-Driven Architecture (Kafka)?", "category": "api-testing", "levels": ["senior"], "theory": False, "source": "new"},

    # ── CI/CD ──────────────────────────────────────────────────────────────
    82:  {"title": "What is Shift Left vs Shift Right testing in a CI/CD pipeline?", "category": "ci-cd", "levels": ["entry"], "theory": True, "source": "pdf"},
    83:  {"title": "What is Pipeline-as-Code and how do you implement it?", "category": "ci-cd", "levels": ["mid"], "theory": False, "source": "pdf"},
    84:  {"title": "What is a Quality Gate in a pipeline?", "category": "ci-cd", "levels": ["entry"], "theory": False, "source": "pdf"},
    86:  {"title": "How do you use Docker containers in your test pipeline?", "category": "ci-cd", "levels": ["senior"], "theory": False, "source": "pdf"},
    87:  {"title": "What is Blue-Green deployment and how do you test it?", "category": "ci-cd", "levels": ["mid"], "theory": False, "source": "pdf"},
    88:  {"title": "How do you monitor pipeline health and reduce build times?", "category": "ci-cd", "levels": ["senior"], "theory": False, "source": "pdf"},
    89:  {"title": "What is a Canary deployment and how do you validate it?", "category": "ci-cd", "levels": ["mid"], "theory": False, "source": "pdf"},
    257: {"title": "CI Basics: how does code move from a local machine to a shared repo safely?", "category": "ci-cd", "levels": ["mid"], "theory": False, "source": "new"},
    258: {"title": "How do you use log aggregation (ELK Stack) to support testing?", "category": "ci-cd", "levels": ["mid","senior"], "theory": False, "source": "pdf"},
    351: {"title": "What is the difference between Continuous Integration, Delivery, and Deployment?", "category": "ci-cd", "levels": ["entry","mid"], "theory": True, "source": "pdf"},
    447: {"title": "How do you enforce coding standards in a large automation repo?", "category": "ci-cd", "levels": ["senior"], "theory": False, "source": "pdf"},
    751: {"title": "How do you implement Programmatic Quality Gates in a pipeline?", "category": "ci-cd", "levels": ["senior"], "theory": False, "source": "new"},
    752: {"title": "How do you test a Canary Deployment using Service Mesh (Istio/Linkerd)?", "category": "ci-cd", "levels": ["senior"], "theory": False, "source": "new"},
    753: {"title": "How do you test Database Migrations in a pipeline without risking data loss?", "category": "ci-cd", "levels": ["mid","senior"], "theory": False, "source": "new"},
    775: {"title": "How do you manage quality in a Continuous Delivery model (no QA freeze)?", "category": "ci-cd", "levels": ["senior"], "theory": False, "source": "new"},
    780: {"title": "What is your strategy for Blue/Green vs Canary Deployment Testing?", "category": "ci-cd", "levels": ["senior"], "theory": False, "source": "new"},

    # ── SYSTEM DESIGN ──────────────────────────────────────────────────────
    269: {"title": "How do you test a system designed for horizontal scalability?", "category": "system-design", "levels": ["mid","senior"], "theory": False, "source": "pdf"},
    350: {"title": "What is the difference between a Monolith and Microservices?", "category": "system-design", "levels": ["entry","mid"], "theory": True, "source": "pdf"},
    349: {"title": "How do you design an API testing strategy for a microservices architecture?", "category": "system-design", "levels": ["senior"], "theory": False, "source": "pdf"},
    440: {"title": "What is Scalability vs Elasticity in cloud architecture?", "category": "system-design", "levels": ["entry","mid"], "theory": False, "source": "pdf"},
    500: {"title": "The Diamond Challenge: design a self-healing test architecture.", "category": "system-design", "levels": ["lead"], "theory": False, "source": "pdf"},
    745: {"title": "How do you design a testing strategy for a Microservices migration?", "category": "system-design", "levels": ["senior","lead"], "theory": False, "source": "new"},
    746: {"title": "How do you test for Data Consistency in a distributed system (CAP Theorem)?", "category": "system-design", "levels": ["senior","lead"], "theory": False, "source": "new"},
    747: {"title": "How do you design a Load Test for a system expecting 1M concurrent users?", "category": "system-design", "levels": ["senior","lead"], "theory": False, "source": "new"},
    763: {"title": "How do you test for Stale Data in a Caching Layer (CDN/Redis)?", "category": "system-design", "levels": ["senior","lead"], "theory": False, "source": "new"},
    764: {"title": "How do you test Rate Limiting and Throttling logic?", "category": "system-design", "levels": ["senior","lead"], "theory": False, "source": "new"},
    765: {"title": "How do you test Read Replicas vs Sharding for Data Integrity?", "category": "system-design", "levels": ["senior","lead"], "theory": False, "source": "new"},
    776: {"title": "How do you test Circuit Breakers in a distributed architecture?", "category": "system-design", "levels": ["senior","lead"], "theory": False, "source": "new"},
    782: {"title": "How do you test Database Sharding and Cross-Shard Queries?", "category": "system-design", "levels": ["senior","lead"], "theory": False, "source": "new"},

    # ── SECURITY TESTING ───────────────────────────────────────────────────
    95:  {"title": "What is SQL Injection and how do you test for it?", "category": "security-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    112: {"title": "Explain Cross-Site Scripting (XSS) and how you test for it.", "category": "security-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    114: {"title": "How do you test for Insecure Deserialization?", "category": "security-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    117: {"title": "What is a CSRF (Cross-Site Request Forgery) attack and how do you test for it?", "category": "security-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    120: {"title": "What is Security Misconfiguration and give an example.", "category": "security-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    310: {"title": "How do you test for Ransomware resilience and Immutable Backups?", "category": "security-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    311: {"title": "What is Penetration Testing and how does it differ from vulnerability scanning?", "category": "security-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    312: {"title": "How do you test for Broken Authentication vulnerabilities?", "category": "security-testing", "levels": ["lead"], "theory": False, "source": "new"},
    313: {"title": "What is OWASP Top 10 and how do you incorporate it into your test plan?", "category": "security-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    314: {"title": "How do you perform a security code review from a QA perspective?", "category": "security-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    316: {"title": "How do you manage stakeholder pressure when security findings threaten a release?", "category": "security-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    317: {"title": "How do you integrate SAST and DAST tools into a CI/CD pipeline?", "category": "security-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    318: {"title": "How do you design a Compliance Testing strategy for GDPR and PCI-DSS?", "category": "security-testing", "levels": ["lead"], "theory": False, "source": "new"},
    757: {"title": "How do you test for JWT vulnerabilities beyond simple expiry?", "category": "security-testing", "levels": ["senior"], "theory": False, "source": "new"},
    781: {"title": "How do you test Cross-Origin Resource Sharing (CORS) policies?", "category": "security-testing", "levels": ["mid","senior"], "theory": False, "source": "new"},

    # ── PERFORMANCE TESTING ────────────────────────────────────────────────
    101: {"title": "What is the difference between Load Testing and Stress Testing?", "category": "performance-testing", "levels": ["entry"], "theory": True, "source": "pdf"},
    103: {"title": "Why do we use the 90th Percentile (P90) instead of Average for response times?", "category": "performance-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    105: {"title": "How do you correlate dynamic values in a JMeter script?", "category": "performance-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    110: {"title": "How do you decide when to stop a performance test?", "category": "performance-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    147: {"title": "How do you test for database connection pool exhaustion?", "category": "performance-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    174: {"title": "What is an Execution Plan (EXPLAIN) and how does it help you test performance?", "category": "performance-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    246: {"title": "How do you test for battery drain in mobile performance testing?", "category": "performance-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    261: {"title": "What is the difference between Latency and Throughput?", "category": "performance-testing", "levels": ["entry"], "theory": True, "source": "pdf"},
    337: {"title": "How do you test AI model inference throttling at scale?", "category": "performance-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    405: {"title": "What is Chaos Engineering and how do you implement it?", "category": "performance-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    407: {"title": "How do you test Kubernetes resiliency (pod failure, node drain)?", "category": "performance-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    430: {"title": "How do you assess Launch Readiness for a high-traffic product release?", "category": "performance-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    624: {"title": "What is the difference between L4 and L7 Load Balancing from a testing perspective?", "category": "performance-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    625: {"title": "How do you handle Hot Keys in a distributed cache like Redis?", "category": "performance-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    736: {"title": "How do you test for Database Lock contention under high concurrency?", "category": "performance-testing", "levels": ["senior"], "theory": False, "source": "pdf"},

    # ── DATA / AI TESTING ──────────────────────────────────────────────────
    91:  {"title": "When do you use an INNER JOIN vs a LEFT JOIN in Data Testing?", "category": "data-ai-testing", "levels": ["entry"], "theory": True, "source": "pdf"},
    92:  {"title": "Explain ACID properties in Database testing.", "category": "data-ai-testing", "levels": ["entry"], "theory": True, "source": "pdf"},
    187: {"title": "How do you test an ETL pipeline for data accuracy?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    188: {"title": "How do you validate data transformation logic in a pipeline?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    189: {"title": "How do you test for data loss in a streaming pipeline?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    190: {"title": "How do you test a feature store for ML model correctness?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    191: {"title": "How do you build a data quality framework for a data lake?", "category": "data-ai-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    199: {"title": "How do you test a recommendation engine for bias and accuracy?", "category": "data-ai-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    449: {"title": "How do you test an AI model for Bias (Algorithmic Fairness)?", "category": "data-ai-testing", "levels": ["mid"], "theory": False, "source": "new"},
    450: {"title": "How do you validate ML model performance drift over time?", "category": "data-ai-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    527: {"title": "How do you test a Natural Language Processing (NLP) model?", "category": "data-ai-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    528: {"title": "What is Shadow Mode testing for AI/ML models?", "category": "data-ai-testing", "levels": ["mid"], "theory": False, "source": "pdf"},
    529: {"title": "How do you implement A/B testing for ML model variants?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    530: {"title": "How do you test for data pipeline idempotency?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    531: {"title": "How do you validate a real-time feature store?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    657: {"title": "How do you build a Quality Maturity Model for a data engineering team?", "category": "data-ai-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    658: {"title": "What is your Post-Mortem philosophy for a catastrophic data failure?", "category": "data-ai-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    659: {"title": "Explain the Lindy Effect in the context of technology selection.", "category": "data-ai-testing", "levels": ["lead"], "theory": False, "source": "pdf"},
    664: {"title": "What is Idempotency in Data Engineering and how do you test it?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},
    667: {"title": "How do you test Data Partitioning strategies for Big Data systems?", "category": "data-ai-testing", "levels": ["lead"], "theory": False, "source": "new"},
    684: {"title": "How do you test the ACID properties of a Delta Lake or Apache Iceberg table?", "category": "data-ai-testing", "levels": ["senior"], "theory": False, "source": "pdf"},

    # ── QA THEORY ──────────────────────────────────────────────────────────
    94:  {"title": "What is the difference between Quality Assurance and Quality Control?", "category": "qa-theory", "levels": ["entry","mid"], "theory": True, "source": "pdf"},
    126: {"title": "What is Accessibility Testing and why does it matter?", "category": "qa-theory", "levels": ["mid"], "theory": True, "source": "pdf"},
    164: {"title": "What is State Transition Testing?", "category": "qa-theory", "levels": ["mid"], "theory": True, "source": "pdf"},
    169: {"title": "How do you design an Exploratory Testing charter?", "category": "qa-theory", "levels": ["mid"], "theory": True, "source": "pdf"},
    170: {"title": "What is Mutation Testing and when would you use it?", "category": "qa-theory", "levels": ["mid"], "theory": True, "source": "pdf"},
    298: {"title": "What is Root Cause Analysis (RCA) and when do you perform one?", "category": "qa-theory", "levels": ["senior"], "theory": True, "source": "pdf"},
    321: {"title": "How do you test Generative AI features for quality and safety?", "category": "qa-theory", "levels": ["senior"], "theory": True, "source": "pdf"},
    754: {"title": "How do you use TMMi to assess a QA department's maturity?", "category": "qa-theory", "levels": ["senior"], "theory": True, "source": "new"},
    755: {"title": "When is the V-Model still relevant and how do you test within it?", "category": "qa-theory", "levels": ["senior"], "theory": True, "source": "new"},
    790: {"title": "Explain the Testing Pyramid and why it matters.", "category": "qa-theory", "levels": ["entry"], "theory": True, "source": "new"},
    791: {"title": "What is the Bug Lifecycle from discovery to closure?", "category": "qa-theory", "levels": ["entry"], "theory": True, "source": "new"},
    792: {"title": "What are the Seven Principles of Testing (e.g. Pesticide Paradox)?", "category": "qa-theory", "levels": ["entry"], "theory": True, "source": "new"},
}


TEMPLATE = """---
id: {id}
title: "{title}"
category: {category}
levels: {levels}
theory: {theory}
source: {source}
---

## Intent

> *Add the intent for this question — what the interviewer is trying to uncover.*

---

## Answer (STAR)

**Situation:** *Add situation context here.*

**Task:** *Add the task or challenge here.*

**Action:** *Add the specific actions taken — tools, methods, frameworks.*

**Result:** *Add the quantified outcome and business impact.*

---

## Seniority Shift

<div class="seniority-shift">

*Add seniority-specific guidance here.*

</div>
"""


def levels_yaml(levels):
    return "[" + ", ".join(levels) + "]"


created = 0
skipped = 0

for qid, meta in sorted(QUESTIONS.items()):
    filename = f"q{qid:03d}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath) and "template" not in filename:
        skipped += 1
        continue

    content = TEMPLATE.format(
        id=qid,
        title=meta["title"].replace('"', '\\"'),
        category=meta["category"],
        levels=levels_yaml(meta["levels"]),
        theory=str(meta["theory"]).lower(),
        source=meta["source"],
    )

    with open(filepath, "w") as f:
        f.write(content)
    created += 1

print(f"✅ Created: {created} question stubs")
print(f"⏭️  Skipped: {skipped} (already exist)")
print(f"📁 Output:  {OUTPUT_DIR}/")
