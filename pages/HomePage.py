from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger
# create a class for the page


class HomePage(BasePage):
    # Create a method that performs the logout action on the page
    def logout(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "div.controls__logout > span").click()
        logger.info('Click on Logout')

    # Create a method that retrieves the side menus on the page
    def get_side_menus(self):
        # Find all the side menus elements
        side_menus = self.driver.find_elements(
            By.CSS_SELECTOR, 'label.aside__label')

        # Create a set of lowercase menu text values and return it
        return {menu.text.lower() for menu in side_menus}
