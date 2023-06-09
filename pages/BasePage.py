from selenium.webdriver.common.by import By
from configs import config
from time import sleep
from logs.logger import logger

# create a class for the page


class BasePage:
    # Create a constructor method for the page object
    def __init__(self, driver) -> None:
        self.driver = driver

    # Method to check if a specific text exists on the page
    def text_exist(self, text):
        wait = 0
        while wait < config.TIMEOUT:
            # Check if the text is not present in the page source
            if text.lower() not in self.driver.page_source.lower():
                sleep(1)
                wait += 1
                logger.info(f"Waited for {wait} seconds ....")
            else:
                # If the text is found, log the information and return True
                logger.info(
                    f"Found the {text} on the page {wait} seconds ....")
                return True

        # If the text is not found within the specified timeout, log the information and return False
        logger.info(
            f'Text [{text}] was not found on the page. Waited for {wait} seconds ... ')
        return False
