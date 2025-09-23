# Автотесты с Playwright

Проект для автоматизированного тестирования веб-приложений с использованием Playwright и pytest.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Dimit-ry/aqa-tests.git
cd aqa-tests
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# или
.\.venv\Scripts\activate.bat  # Windows CMD
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
playwright install
```

## Запуск тестов

Запуск всех тестов:
```bash
pytest
```

Запуск с подробным выводом:
```bash
pytest -v
```

Запуск конкретного теста:
```bash
pytest site_calc_test.py -v
```

## Структура проекта

- `site_calc_test.py` - тест калькулятора на сайте cartaxi.io
- `requirements.txt` - зависимости проекта
- `.gitignore` - файлы, игнорируемые Git
- `README.md` - описание проекта

## Браузеры

Playwright поддерживает тестирование в:
- Chromium
- Firefox
- WebKit (Safari)

По умолчанию тесты запускаются во всех браузерах.