import allure
from ..pages.base_page import BasePage
from ..locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_to_password_recovery_button(self):
        self.click_to_element(self.locators.PASSWORD_RECOVERY_BUTTON)
