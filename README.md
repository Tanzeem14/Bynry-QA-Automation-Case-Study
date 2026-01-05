# bynry-qa-automation-case-study
## Part 1: Debugging Flaky Test Code

**Objective:**  
Analyze and fix flaky Playwright UI tests that fail intermittently in CI/CD environments for a multi-tenant B2B SaaS application.

**Summary of Improvements:**
- Added explicit waits for navigation and dynamically loaded UI elements
- Improved test stability for CI pipelines using headless browser execution
- Ensured test isolation using fresh browser contexts
- Handled tenant-specific loading delays
- Considered optional 2FA login scenarios

📄 **Detailed analysis and reasoning:**  
`docs/part1_flaky_test_analysis.md`

🧪 **Test implementation:**  
`tests/ui/test_login_part1.py`

## Part 2: Test Framework Design

Designed a scalable automation framework for a multi-tenant B2B SaaS platform.

**Highlights:**
- Supports Web, Mobile, and API testing
- Handles multiple tenants and user roles
- Integrates with BrowserStack
- CI/CD-ready design

📄 Detailed design:
`docs/part2_framework_design.md`
