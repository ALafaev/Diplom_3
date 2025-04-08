from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def wait_url_to_be(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_for_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    def get_text_of_the_element(self, locator):
        return self.driver.find_element(*locator).text

    def filling_the_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def click_to_element_few_tries(self, locator):
        attempts = 3
        for _ in range(attempts):
            try:
                self.driver.find_element(*locator).click()
                break  # Успешный клик, завершаем цикл
            except ElementClickInterceptedException:
                sleep(2)  # Ожидание перед следующей попыткой

    def wait_for_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(locator))

    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        drag_and_drop(self.driver, source, target)

    def wait_for_text_to_be_present_in_element(self, locator, text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
