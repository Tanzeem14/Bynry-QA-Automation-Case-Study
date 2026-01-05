# Part 3: API + UI Integration Test

## Overview

This section validates the complete project creation flow across multiple layers of a multi-tenant B2B SaaS platform.

The test ensures that:
- A project created via API appears correctly in the Web UI
- The same project is accessible on mobile devices
- The project is visible only to the correct tenant (tenant isolation)

---

## 1. Test Strategy

The integration test combines:
- **API testing** (pytest + requests)
- **Web UI validation** (Playwright)
- **Mobile validation** (BrowserStack)

The test follows a single end-to-end business flow rather than isolated component testing.

---

## 2. Test Flow

1. Create a project using backend API
2. Verify project appears in Web UI for the correct tenant
3. Verify project is accessible on mobile device
4. Verify project is NOT visible to other tenants

---

## 3. Test Data Management

- Test data is created dynamically via API
- Project ID returned from API is reused across UI validations
- Cleanup is assumed via API after test execution
- Unique project names prevent test data collision

---

## 4. Cross-Platform Validation

- Web UI is validated using Playwright
- Mobile UI is validated using BrowserStack
- Same backend data is verified across platforms

---

## 5. Tenant Isolation Validation

- Project visibility is validated only under the correct tenant
- Login to another tenant confirms the project is not accessible
- Ensures data security boundaries between tenants

---

## 6. Assumptions

- Authentication tokens are available for API calls
- Test users exist for each tenant
- Mobile tests are executed on BrowserStack
- Cleanup APIs are available or test data is auto-expired

---

## 7. Edge Cases Considered

- Slow API response or network latency
- Delayed UI rendering after backend updates
- Mobile responsiveness and screen size differences
- API failures handled via status code validation

---

## 8. Key Takeaway

Combining API and UI validation ensures data integrity, correct system integration, and consistent user experience across platforms.
