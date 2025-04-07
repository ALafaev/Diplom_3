import allure
from selenium import webdriver
from urls import PageUrls
import pytest

@pytest.fixture(params=['firefox', 'chrome'], autouse=True) # Запуск браузера
def driver(request):
    driver = None
    with allure.step(f'Запуск браузера {request.param}'):
        if request.param == "firefox":
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(PageUrls.HOME_PAGE)
        elif request.param == 'chrome':
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(PageUrls.HOME_PAGE)

    yield driver
    with allure.step(f'Закрытие браузера {request.param}'):
        driver.quit()