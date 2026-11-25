import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import MainPageLocators
from urls import MAIN_URL


class TestConstructor:

    @pytest.mark.parametrize('tab, tab_name', [
        (MainPageLocators.SAUCES_TAB, 'Соусы'),
        (MainPageLocators.FILLINGS_TAB, 'Начинки'),
    ])
    def test_constructor_click_tab_section_selected(self, driver, tab, tab_name):
        driver.get(MAIN_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tab)).click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.CURRENT_TAB, tab_name))
        assert driver.find_element(*MainPageLocators.CURRENT_TAB).text == tab_name

    def test_constructor_click_buns_tab_buns_selected(self, driver):
        driver.get(MAIN_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)).click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.CURRENT_TAB, 'Булки'))
        assert driver.find_element(*MainPageLocators.CURRENT_TAB).text == 'Булки'
