import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import NAME
from helpers import generate_email, generate_password
from locators import RegisterPageLocators
from urls import LOGIN_URL, REGISTER_URL


class TestRegistration:

    def test_registration_valid_data_redirect_to_login_page(self, driver):
        driver.get(REGISTER_URL)
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_password())
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_registration_short_password_error_shown(self, driver, password):
        driver.get(REGISTER_URL)
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR))
        assert error.text == 'Некорректный пароль'
