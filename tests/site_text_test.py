import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://cartaxi.io/")
    expect(page.locator("#mainForm")).to_contain_text("Вызвать эвакуатор в Москва")
    expect(page.locator("#mainForm")).to_contain_text("Откуда забрать")
    expect(page.locator("#mainForm")).to_contain_text("Куда доставить")
    expect(page.locator("#category")).to_contain_text("Что перевозим")
    expect(page.locator("#mainForm")).to_contain_text("Блокировка колес")
    expect(page.locator("#mainForm")).to_contain_text("Не могут вращаться")
    expect(page.locator("#tariffs")).to_contain_text("Стандарт")
