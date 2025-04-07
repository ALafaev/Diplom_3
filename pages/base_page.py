from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def wait_url_to_be(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url

    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_for_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    def check_url_contains_value(self, value):
        WebDriverWait(self.driver, 10).until(EC.url_contains(value))

    def get_text_of_the_element(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def filling_the_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_element_is_enabled(self, locator):
        return self.driver.find_element(*locator).is_enabled()
