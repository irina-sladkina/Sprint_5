import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import HeaderLocators, MainPageLocators, ProfilePageLocators
from urls import PROFILE_URL


class TestPersonalAccount:

    def test_go_to_personal_account_profile_opened(self, logged_in_driver):
        logged_in_driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(PROFILE_URL))
        assert logged_in_driver.find_element(*ProfilePageLocators.PROFILE_LINK).is_displayed()

    @pytest.mark.parametrize('link', [HeaderLocators.CONSTRUCTOR_LINK, HeaderLocators.LOGO])
    def test_go_from_personal_account_to_constructor_constructor_opened(self, logged_in_driver, link):
        logged_in_driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(PROFILE_URL))
        WebDriverWait(logged_in_driver, 10).until(EC.element_to_be_clickable(link)).click()
        title = WebDriverWait(logged_in_driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert title.is_displayed()
