import uuid
import requests
from playwright.sync_api import sync_playwright, expect

# ============================================================
# ASSUMPTIONS
# - Staging environment allows API-based test data creation
# - Authentication token is available (mocked here)
# - Tenant subdomains exist:
#     company1.workflowpro.com
#     company2.workflowpro.com
# - 2FA is disabled for test users
# - Mobile validation is executed via BrowserStack in CI
#   (simulated here using mobile viewport)
# ============================================================

API_URL = "https://api.workflowpro.com/v1/projects"
AUTH_TOKEN = "fake_test_token_for_staging"

TENANT_1 = "company1"
TENANT_2 = "company2"


def test_project_creation_flow():
    """
    End-to-end integration test:
    1. Create project via API
    2. Verify project appears in Web UI
    3. Verify project accessibility on Mobile (conceptual)
    4. Verify tenant isolation (security)
    """

    # --------------------------------------------------------
    # 1. API: Create a unique project
    # --------------------------------------------------------
    project_name = f"Test Project - {uuid.uuid4().hex[:8]}"

    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "X-Tenant-ID": TENANT_1
    }

    payload = {
        "name": project_name,
        "description": "Created via automated integration test",
        "team_members": ["user1@company1.com"]
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    assert response.status_code == 201, f"Project creation failed: {response.text}"

    project_id = response.json().get("id")
    assert project_id is not None

    try:
        # --------------------------------------------------------
        # 2. Web UI: Verify project appears for correct tenant
        # --------------------------------------------------------
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://company1.workflowpro.com/login")
            page.fill("#email", "admin@company1.com")
            page.fill("#password", "password123")
            page.click("#login-btn")

            page.wait_for_url("**/dashboard*", timeout=20000)

            page.goto("https://company1.workflowpro.com/projects")
            page.wait_for_selector(f"text={project_name}", timeout=10000)

            expect(page.locator(f"text={project_name}")).to_be_visible()

            # --------------------------------------------------------
            # 3. Mobile Validation (BrowserStack - Conceptual)
            # --------------------------------------------------------
            # Simulating mobile view locally.
            # In CI, this step would execute on BrowserStack
            # using a real iOS/Android device.
            page.set_viewport_size({"width": 390, "height": 844})  # iPhone 14
            expect(page.locator(f"text={project_name}")).to_be_visible()

            context.close()
            browser.close()

        # --------------------------------------------------------
        # 4. Security: Tenant Isolation Validation
        # --------------------------------------------------------
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://company2.workflowpro.com/login")
            page.fill("#email", "user@company2.com")
            page.fill("#password", "password123")
            page.click("#login-btn")

            page.wait_for_url("**/dashboard*", timeout=20000)

            page.goto("https://company2.workflowpro.com/projects")
            page.wait_for_selector(".project-card", timeout=10000)

            page_content = page.content()
            assert project_name not in page_content, (
                "Security violation: Project visible in wrong tenant"
            )

            context.close()
            browser.close()

    finally:
        # --------------------------------------------------------
        # Cleanup: Remove test data
        # --------------------------------------------------------
        requests.delete(f"{API_URL}/{project_id}", headers=headers)
