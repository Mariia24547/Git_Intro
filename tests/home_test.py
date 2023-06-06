from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from logs.logger import logger


# create test cases
def test_user_logout(driver):
    
    login_page = LoginPage(driver)
    login_page.user_login()
    sleep(5)
    
    home_page = HomePage(driver)
    home_page.logout()
    sleep(5)
    
    assert driver.find_element(By.CSS_SELECTOR, 'div.heading > h1').text == 'Login'


def test_user_allowed_menus(driver):
    login_page = LoginPage(driver)
    login_page.user_login()
    sleep(5)
    home_page = HomePage(driver)
    expected_user_menus = {'accounts', 'cards', 'transfers', 'reports', 'news', 'my profile'}
    displayed_user_menus = home_page.get_side_menus()
    logger.info(f'Expected {expected_user_menus}')
    logger.info(f'Displayed{displayed_user_menus}')

    diff = expected_user_menus ^ displayed_user_menus
    assert len(diff)== 0



    def test_user_allowed_menus(driver):
        login_page = LoginPage(driver)
        login_page.admin_login()
        sleep(5)
        home_page = HomePage(driver)
        expected_admin_menus = {'accounts', 'messages', 'transfers', 'reports', 'news', 'profiles', 'requests', 'settings', 'system log'}
        displayed_admin_menus = home_page.get_side_menus()
        diff = expected_admin_menus ^ displayed_admin_menus
        assert len(diff) == 0
    
