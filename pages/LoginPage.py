from selenium.webdriver.common.by import By
from time import sleep
from pages.BasePage import BasePage
from logs.logger import logger
from configs import config
# create a class for the page


class LoginPage(BasePage):
    # Class attributes for locating elements on the page
    email_field = By.CSS_SELECTOR, "[type='email']"
    password_field = By.CSS_SELECTOR, "[type='password']"
    submit_button = By.CSS_SELECTOR, "[type='submit']"

    # Method for performing login with provided username and password
    def login(self, username, password):
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        logger.info(f'Entered username: {username} and password: {password}')
        self.driver.find_element(*self.submit_button).click()
        logger.info('Click on Sign in button')

    # Method for performing user login using the configured user credentials
    def user_login(self):
        self.login(config.USER, config.USER_PASSWORD)

    # Method for performing admin login using the configured admin credentials
    def admin_login(self):
        self.login(config.ADMIN, config.ADMIN_PASSWORD)
