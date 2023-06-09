import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.AccountsPage import AccountsPage
from pages.AccountsPage import AccountsInfo
from logs.logger import logger


account_numbers = ['EBQ11113487654', 'EBQ11223487456',
                   'EBQ11223387654', 'EBQ38495629375', '511264340']


# @pytest.mark.skip
@pytest.mark.parametrize("account_number", account_numbers)
def test_account_selection(driver, account_number):
    login_page = LoginPage(driver)
    login_page.user_login()
    sleep(5)
    accounts_page = AccountsPage(driver)
    accounts_page.select_account(account_number)

    displayed_account_number = driver.find_element(
        By.XPATH, "//span[text()='Account number']/following-sibling::span[1]").text
    assert displayed_account_number == account_number
    logger.info(f"Account number: {displayed_account_number}")
