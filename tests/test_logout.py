from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import HeaderLocators, LoginPageLocators, ProfilePageLocators
from urls import LOGIN_URL


class TestLogout:

    def test_logout_from_personal_account_login_page_opened(self, logged_in_driver):
        logged_in_driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(logged_in_driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert logged_in_driver.find_element(*LoginPageLocators.TITLE).is_displayed()
