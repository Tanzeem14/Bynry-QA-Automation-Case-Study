import requests
import pytest
from playwright.sync_api import sync_playwright, expect

API_URL = "https://api.workflowpro.com/api/v1/projects"
TOKEN = "dummy-token"
TENANT_1 = "company1"
TENANT_2 = "company2"

PROJECT_NAME = "API Created Test Project"


def test_project_creation_flow():
    # 1. API: Create project
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "X-Tenant-ID": TENANT_1
    }

    payload = {
        "name": PROJECT_NAME,
        "description": "Project created via API",
        "team_members": []
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    assert response.status_code == 200

    project_id = response.json().get("id")
    assert project_id is not None

    # 2. Web UI: Verify project appears for correct tenant
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://company1.workflowpro.com/login")
        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        page.wait_for_url("**/dashboard*", timeout=20000)
        page.fill("#search-project", PROJECT_NAME)

        expect(page.locator(".project-card")).to_contain_text(PROJECT_NAME)

        context.close()
        browser.close()

    # 3. Tenant Isolation: Verify project not visible in another tenant
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://company2.workflowpro.com/login")
        page.fill("#email", "admin@company2.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        page.wait_for_url("**/dashboard*", timeout=20000)
        page.fill("#search-project", PROJECT_NAME)

        assert page.locator(".project-card").count() == 0

        context.close()
        browser.close()

    # Note:
    # Mobile validation would be executed using BrowserStack
    # with similar assertions on the mobile UI
