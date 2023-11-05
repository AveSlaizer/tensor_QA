import pytest
from selenium import webdriver

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}


def pytest_addoption(parser):
    """
    Добавление дополнительных опций запуска тестов.
        --browser_name=<browser_name> - запуск тестов на определенном браузере, по умолчанию Chrome.
    """
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="class")
def browser(request):
    """
    Возвращает объект WebDriver, с указанными в командной строке опциям.
    """
    browser_name = request.config.getoption("browser_name")

    if browser_name in supported_browsers:
        browser = supported_browsers.get(browser_name)()
        print(f"\nStart {browser_name} browser for test..")
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    yield browser

    print("\nQuit browser..")
    browser.quit()
