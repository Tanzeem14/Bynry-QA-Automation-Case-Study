# QA Automation Case Study – Bynry Internship

## Overview
This repository contains my solution for the **QA Automation Engineering Intern – Case Study** at **Bynry Inc**.

The case study focuses on:
- Fixing flaky UI tests
- Designing a scalable test automation framework
- Implementing an API + UI integration test for a multi-tenant B2B SaaS platform

---

## Tech Stack
- Python 3.9+
- pytest (test runner)
- Playwright (web UI automation)
- requests (API testing)
- BrowserStack (cross-browser & mobile testing – conceptual)

---

## How to Run

### Setup
```bash
pip install -r requirements.txt
playwright install
```

### Part 1: Flaky Test Fix
```bash
pytest tests/ui/test_login_part1.py -v
```
### Part 2 (Framework Design) is documented in `docs/part2_framework_design.md`.

### Part 3: API + UI Integration Test (Conceptual)
```bash
pytest tests/api/test_project_creation_flow.py -v
```

### Structure
```text 
tests/
 ├── ui/                 → Flaky login test fix
 ├── api/                → API + UI integration test
docs/
 ├── part1_flaky_test_analysis.md
 ├── part2_framework_design.md
 └── part3_api_ui_integration.md
```
### Notes

APIs, tenants, and authentication are assumed for case study purposes

BrowserStack execution is conceptual and intended for CI/CD pipelines

Focus is on test design, structure, and automation strategy