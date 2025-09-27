import pytest
from playwright.sync_api import Browser, Page, sync_playwright


@pytest.fixture(scope="session")
def browser():
    """Создает headless Chrome браузер для всех тестов"""
    with sync_playwright() as playwright:
        # Запускаем браузер в headless режиме с дополнительными флагами для CI
        browser = playwright.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-dev-shm-usage']  # Для стабильности в CI
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser):
    """Создает новую страницу для каждого теста"""
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def browser_headed():
    """Создает видимый Chrome браузер для локальной отладки"""
    with sync_playwright() as playwright:
        # Запускаем браузер с видимым окном
        browser = playwright.chromium.launch(
            headless=False,  # Видимый режим
            slow_mo=500      # Замедление для лучшей видимости действий
        )
        yield browser
        browser.close()


@pytest.fixture
def page_headed(browser_headed: Browser):
    """Создает новую страницу в видимом браузере"""
    page = browser_headed.new_page()
    yield page
    page.close()
