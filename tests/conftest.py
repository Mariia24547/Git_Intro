import pytest
from selenium import webdriver
from datetime import datetime
import os
from logs.logger import logger
from configs import config

@pytest.fixture()
def driver():
    driver = driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')
    logger.info('Opened Firefox Browser')
    driver.get(config.URL)
    
    driver.implicitly_wait(config.TIMEOUT)
    driver.maximize_window()


    yield driver

    #driver.save_screenshot(r'.\evidence\screenshot.png')
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    driver.save_screenshot(fr".\evidence\{test_name}-{timestamp}.png")

    driver.quit()
    logger.info('Close the Browser')