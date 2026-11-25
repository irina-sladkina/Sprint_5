from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")  # Ссылка «Конструктор» в шапке
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")  # Логотип Stellar Burgers
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # Ссылка «Личный кабинет» в шапке


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт»
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ» (видна после входа)
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок «Соберите бургер»
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка «Начинки»
    CURRENT_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # Выбранная вкладка конструктора


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле «Пароль»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка «Некорректный пароль»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» под формой регистрации


class LoginPageLocators:
    TITLE = (By.XPATH, "//h2[text()='Вход']")  # Заголовок «Вход»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле «Пароль»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» на странице восстановления пароля


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Ссылка «Профиль» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выход»
