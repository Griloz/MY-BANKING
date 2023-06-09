from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from logs.logger import logger

# importing the LoginPage class from LoginPage file
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


# create test cases

def test_user_logout(driver):
    # Create an instance of LoginPage class
    login_page = LoginPage(driver)
    # Perform user login
    login_page.user_login()
    sleep(5)
    # Create an instance of HomePage class
    home_page = HomePage(driver)
    # Perform logout
    home_page.logout()
    sleep(5)
    # Assert that the user is redirected to the login page after logout
    assert driver.find_element(
        By.CSS_SELECTOR, 'div.heading > h1').text == 'Login'


def test_user_allowed_menus(driver):
    # Create an instance of LoginPage class
    login_page = LoginPage(driver)
    # Perform user login
    login_page.user_login()
    sleep(5)
    # Create an instance of HomePage class
    home_page = HomePage(driver)
    # Define the expected user menus
    expected_user_menus = {'accounts', 'cards',
                           'transfers', 'reports', 'news', 'my profile'}
    # Get the displayed user menus from the home page
    displayed_user_menus = home_page.get_side_menus()
    logger.info(f'Expected {expected_user_menus}')
    logger.info(f'Displayed {displayed_user_menus}')
    # Compare the expected and displayed user menus
    diff = expected_user_menus ^ displayed_user_menus
    assert len(diff) == 0


def test_admin_allowed_menus(driver):
    # Create an instance of LoginPage class
    login_page = LoginPage(driver)
    # Perform admin login
    login_page.admin_login()
    sleep(5)
    # Create an instance of HomePage class
    home_page = HomePage(driver)
    # Define the expected admin menus
    expected_admin_menus = {'accounts', 'messages', 'transfers',
                            'reports', 'news', 'profiles', 'requests', 'settings', 'system log'}
    # Get the displayed admin menus from the home page
    displayed_admin_menus = home_page.get_side_menus()
    logger.info(f'Expected {expected_admin_menus}')
    logger.info(f'Displayed {displayed_admin_menus}')
    # Compare the expected and displayed admin menus
    diff = expected_admin_menus ^ displayed_admin_menus
    assert len(diff) == 0
