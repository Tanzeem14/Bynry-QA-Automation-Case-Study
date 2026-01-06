# Part 2: Test Automation Framework Design

## Overview

This section describes the design of a scalable and maintainable test automation framework for a **multi-tenant B2B SaaS platform** like WorkFlow Pro.

The framework is designed to support:
- Web and mobile UI testing
- API testing
- Multiple tenants and user roles
- Cross-browser and cross-device execution using BrowserStack
- CI/CD pipeline integration

The goal is to ensure reliability, scalability, and ease of maintenance as the application grows.

---

## 1. Framework Architecture Overview

The framework follows a **hybrid approach** combining:
- Page Object Model (POM) for UI automation
- Data-driven testing for roles, tenants, and environments
- API + UI integration testing
- Pytest fixtures for setup and teardown

This design allows clear separation of concerns and supports parallel execution in CI/CD pipelines.

---

## 2. Folder Structure Design

```text
automation-framework/
├── config/
│   ├── env.yaml
│   ├── users.yaml
│   └── browserstack.yaml
│
├── core/
│   ├── base_test.py
│   ├── driver_factory.py
│   └── api_client.py
│
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
│
├── mobile_screens/
│   └── login_screen.py
│
├── tests/
│   ├── ui/
│   ├── api/
│   └── mobile/
│
├── utils/
│   ├── config_loader.py
│   └── logger.py
│
├── reports/
├── pytest.ini
└── requirements.txt
```

## 3.Configuration Management

To handle multiple environments, browsers, and test data, the framework uses external configuration files and utility loaders.

config/
├── env.yaml            # Environment and tenant URLs
├── users.yaml          # Test users and roles
├── browserstack.yaml   # Browser and device configurations

- Multiple environments are handled using env.yaml, which stores base URLs for different tenants (company1, company2, etc.).

- Multiple browsers and devices are managed through browserstack.yaml and selected at runtime via configuration or CI parameters.

- Test data and user roles (Admin, Manager, Employee) are stored in users.yaml and loaded dynamically for data-driven tests.

- A shared configuration loader reads these files so the same tests can run across different setups without code changes.

## 4. Missing Requirements & Clarifying Questions

- How will we manage test data so tests don’t fail because of old or duplicate data?
- Can we use production-like data, or should all tests rely on mock data?
- How many tests should run in parallel in CI/CD?
- Are there any limits on running tests in parallel across multiple tenants?
- What type of test reports are expected (HTML, Allure, CI-native)?
- Should test reports be stored or shared after pipeline execution?
- Does the application use SSO or 2FA for login, and should automation handle it?
- Can API tokens or backend APIs be used to speed up authentication?
- Should mobile tests run on real devices or emulators/simulators?
- Are we testing native mobile apps or mobile web?
- Which CI/CD tool will be used (Jenkins, GitHub Actions, GitLab, etc.)?
- Are there any quality gates like minimum pass percentage or flaky test retries?