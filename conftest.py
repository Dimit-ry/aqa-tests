import pytest
from playwright.sync_api import Browser, Page, sync_playwright


@pytest.fixture(scope="session")
def browser():
    """Создает headless Chrome браузер для всех тестов"""
    with sync_playwright() as playwright:
        # Запускаем браузер в headless режиме (без окна)
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser):
    """Создает новую страницу для каждого теста"""
    page = browser.new_page()
    yield page
    page.close()