import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    # Тест калькулятора стоимости на сайте cartaxi.io - крутой коммент но с правками калеки
    page.goto("https://cartaxi.io/")
    page.get_by_role("navigation").get_by_text("Услуги").click()
    page.get_by_role("link", name="Калькулятор").click()
    page.get_by_role("link", name="Рассчитать стоимость").click()
    page.locator("input[type=\"text\"]").nth(1).click()
    page.locator("input[type=\"text\"]").nth(1).fill("Пролетарская спб")
    
    # Пробуем найти кнопку очистки, если есть - кликаем, если нет - очищаем через keyboard
    try:
        clear_button = page.locator(".form-item__right-clear-btn")
        clear_button.wait_for(state="visible", timeout=3000)
        clear_button.click()
    except:
        # Если кнопки нет, очищаем поле через клавиатуру (Ctrl+A + Delete)
        page.locator("input[type=\"text\"]").nth(1).click()
        page.keyboard.press("Control+a")
        page.keyboard.press("Delete")
    
    page.locator("input[type=\"text\"]").nth(1).fill("Пролетарская")
    page.get_by_text("метро Пролетарская, Таганско-Краснопресненская линия, Москва").click()
    page.locator("input[type=\"text\"]").nth(2).click()
    page.locator("input[type=\"text\"]").nth(2).fill("Ладожская")
    page.get_by_text("Ладожская улица, Москва").click()
    page.locator(".modal-categories-list__categories-item").first.click()
    page.get_by_role("button", name="Подтвердить").click()
    page.locator(".counter-inc").click()
    page.locator(".counter-inc").click()
    page.locator(".counter-inc").click()
    page.locator(".counter-inc").click()
