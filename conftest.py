import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import NAME
from helpers import generate_email, generate_password
from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators
from urls import LOGIN_URL, REGISTER_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    email = generate_email()
    password = generate_password()
    driver.get(REGISTER_URL)
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(NAME)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
    return email, password


@pytest.fixture
def logged_in_driver(driver, registered_user):
    email, password = registered_user
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
    return driver
