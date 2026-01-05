# Bynry QA Automation Case Study

This repository contains my solution for the **QA Automation Engineering Intern – Case Study** at **Bynry Inc**.

The case study evaluates test automation skills for a **multi-tenant B2B SaaS platform**, focusing on test reliability, framework design, API + UI integration, and CI/CD readiness.

---

## 🛠️ Technologies Used

- **Python**
- **pytest** – test runner
- **Playwright** – web UI automation
- **requests** – API testing
- **BrowserStack** – cross-browser and mobile testing (conceptual)
- **GitHub** – version control

---

## Part 1: Debugging Flaky Test Code

**Objective:**  
Analyze and fix flaky Playwright UI tests that fail intermittently in CI/CD environments.

**Summary of Improvements:**
- Added explicit waits for navigation and dynamic UI elements
- Improved CI stability using headless execution
- Ensured test isolation using browser contexts
- Handled tenant-specific loading delays
- Considered optional 2FA scenarios

📄 Detailed analysis:  
`docs/part1_flaky_test_analysis.md`

🧪 Test implementation:  
`tests/ui/test_login_part1.py`

---

## Part 2: Test Framework Design

Designed a scalable and maintainable test automation framework for a multi-tenant B2B SaaS platform.

**Highlights:**
- Supports Web, Mobile, and API testing
- Handles multiple tenants and user roles
- Integrates with BrowserStack
- CI/CD-ready and scalable design

📄 Detailed framework design:  
`docs/part2_framework_design.md`

---

## Part 3: API + UI Integration Test

Designed an end-to-end integration test validating project creation across backend API and frontend UI layers.

**Coverage:**
- Project creation via backend API
- Web UI validation using Playwright
- Tenant isolation verification
- Cross-platform testing considerations

📄 Detailed approach:  
`docs/part3_api_ui_integration.md`

🧪 Test implementation:  
`tests/api/test_project_creation_flow.py`

---

## 📌 Notes & Assumptions

- The platform and APIs are assumed for case study purposes
- Valid authentication tokens and test users are assumed
- Mobile execution via BrowserStack is conceptual
- The focus is on **test design, structure, and strategy**, not execution against a live system
