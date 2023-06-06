from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger

class HomePage(BasePage):
    

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, "div.controls__logout > span").click()
        logger.info('Clicked on Logout Button')
    

    def get_side_menus(self):
        side_menus = self.driver.find_element(By.CSS_SELECTOR,'label.aside__label')
        return{menu.text for menu in side_menus}