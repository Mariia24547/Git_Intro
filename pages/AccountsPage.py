from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger

class AccountPage(BasePage):
    

    def select_account(self):


        self.driver.find_element(By.CSS_SELECTOR, "[formcontrolname='accountId']").click()
        
        