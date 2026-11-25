import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import (ForgotPasswordPageLocators, HeaderLocators, LoginPageLocators,
                      MainPageLocators, RegisterPageLocators)
from urls import FORGOT_PASSWORD_URL, MAIN_URL, REGISTER_URL


class TestLogin:

    @pytest.mark.parametrize('start_url, login_entry', [
        (MAIN_URL, MainPageLocators.LOGIN_BUTTON),
        (MAIN_URL, HeaderLocators.PERSONAL_ACCOUNT_LINK),
        (REGISTER_URL, RegisterPageLocators.LOGIN_LINK),
        (FORGOT_PASSWORD_URL, ForgotPasswordPageLocators.LOGIN_LINK),
    ])
    def test_login_from_different_entry_points_order_button_shown(self, driver, registered_user,
                                                                  start_url, login_entry):
        email, password = registered_user
        driver.get(start_url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(login_entry)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
