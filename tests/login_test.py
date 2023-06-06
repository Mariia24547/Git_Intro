from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from time import sleep
import pytest
from configs import config

def test_login_page(driver):
    
    assert driver.find_element(By.CSS_SELECTOR, 'div.heading > h1').text =='Login'




def test_admin_login(driver):

    login_page = LoginPage(driver)
    login_page.admin_login()
    assert driver.find_element(By.CSS_SELECTOR, 'div.controls__logout > span').text == 'Log Out'




def test_login_with_username_less_than_4_chars(driver):
    login_page = LoginPage(driver)
    login_page.login_with_username_less_than_4_chars()
    sleep(5)
    assert 'Should be minimum 4 chars.' in driver.page_source


invalid_login_parameters = [
    ('', 'test', 'Field is required'),
    ('aa', 'test', 'Should be minimum 4 chars'),
    ('Test', 'Test', 'Wrong username or password'),
    #('Test', '', 'Field is required'),
    #('*&^hj', 'IUH*&(*)', 'Wrong username or password'),
]

@pytest.mark.parametrize("username, password, checkpoint", invalid_login_parameters)
def test_invalid_login(driver,username, password, checkpoint):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    sleep(5)
    assert checkpoint in driver.page_source