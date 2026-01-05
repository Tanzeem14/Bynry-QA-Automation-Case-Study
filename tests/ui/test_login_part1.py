import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://app.workflowpro.com/login"

ADMIN_USER = {
    "email": "admin@company1.com",
    "password": "password123"
}

COMPANY2_USER = {
    "email": "user@company2.com",
    "password": "password123"
}

def test_user_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            BASE_URL,
            timeout=30000,
            wait_until="networkidle"
        )

        page.fill("#email", ADMIN_USER["email"])
        page.fill("#password", ADMIN_USER["password"])
        page.click("#login-btn")

        # Optional handling for 2FA users
        if page.locator("#otp-input").is_visible():
            pytest.skip("2FA enabled for this user")

        page.wait_for_url("**/dashboard*", timeout=15000)

        welcome = page.locator(".welcome-message")
        expect(welcome).to_be_visible(timeout=10000)

        context.close()
        browser.close()


def test_multi_tenant_access():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            BASE_URL,
            timeout=30000,
            wait_until="networkidle"
        )

        page.fill("#email", COMPANY2_USER["email"])
        page.fill("#password", COMPANY2_USER["password"])
        page.click("#login-btn")

        page.wait_for_url("**/dashboard*", timeout=15000)
        page.wait_for_selector(".project-card", timeout=15000)

        projects = page.locator(".project-card")
        count = projects.count()
        assert count > 0

        for i in range(count):
            assert "Company2" in projects.nth(i).text_content()

        context.close()
        browser.close()
