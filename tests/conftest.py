import pytest
from selenium import webdriver
from datetime import datetime
import os
from logs.logger import logger
from configs import config


@pytest.fixture()
def driver():
    # steps to run before each test case, setup
    test_name = os.environ.get(
        'PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    logger.info(f'########### Test Case: {test_name} ###########')

    driver = webdriver.Firefox()
    logger.info('Opened Firefox Browser')
    driver.get(config.URL)
    logger.info('Launched the e-banq app')
    driver.implicitly_wait(config.TIMEOUT)
    driver.maximize_window()

    # pass/give the driver to the test case
    yield driver

    # steps to run after each test case, teardown

    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    driver.save_screenshot(fr".\evidence\{test_name}-{timestamp}.png")
    driver.quit()
    logger.info('Closed browser')
