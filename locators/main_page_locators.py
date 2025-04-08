from selenium.webdriver.common.by import By

class MainPageLocators:
    HEADER_MAKE_YOUR_BURGER = (By.XPATH, './/h1[text()="Соберите бургер"]')  # Заголовок "Соберите бургер"
    RANDOM_INGREDIENT = (By.XPATH, './/ul[contains(@class,"BurgerIngredients")][1]/a[1]')
    RANDOM_INGREDIENT_COUNTER = (By.XPATH, './/ul[contains(@class,"BurgerIngredients")][1]/a[1]//p[contains(@class,"counter__num")]')
    INGREDIENT_DETAILS_POPUP_HEADER = (By.XPATH, './/h2[contains(@class,"modal__title") and text()="Детали ингредиента"]')
    CLOSE_POPUP_BUTTON = (By.XPATH, './/button[contains(@class,"modal__close")]')
    BURGER_CONSTRUCTOR_SECTION = (By.XPATH, './/section[contains(@class,"BurgerConstructor")]/ul')
    ORDER_IDENTIFIER_TITLE = (By.XPATH, './/section[contains(@class,"modal_opened")]//p[text()="идентификатор заказа"]')
    MAKE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # Кнопка "Оформить заказ" (пользователь авторизован)