import pytest
from selenium.webdriver.common.by import By
from time import sleep

from pages.LoginPage import LoginPage
# from .conftest import setup


def test_login_page(driver):
    sleep(2)
    assert driver.find_element(
        By.CSS_SELECTOR, 'div.heading > h1').text == 'Login'


def test_user_login(driver):
    login_page = LoginPage(driver)
    login_page.user_login()
    assert driver.find_element(
        By.CSS_SELECTOR, 'div.controls__logout > span').text == 'Log Out'


def test_admin_login(driver):
    login_page = LoginPage(driver)
    login_page.admin_login()
    assert driver.find_element(
        By.CSS_SELECTOR, 'div.controls__logout > span').text == 'Log Out'


invalid_login_parameters = [
    ('', 'test', 'Field is required'),
    ('aa', 'test', 'Should be minimum 4 chars'),
    ('test', 'test', 'Wrong username or password'),
    ('', '', 'Field is required.'),
]


@pytest.mark.parametrize("username, password, checkpoint", invalid_login_parameters)
def test_invalid_login(driver, username, password, checkpoint):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    # sleep(5)
    # assert checkpoint in driver.page_source
    assert login_page.text_exist(checkpoint)
