import allure

from ..pages.base_page import BasePage
from ..locators.header_locators import HeaderLocators

class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderLocators

    @allure.step('Клик по кнопке "Личный кабинет" в хедере страницы')
    def click_to_personal_account_button(self):
        self.click_to_element_few_tries(self.locators.PERSONAL_ACCOUNT_BUTTON)
