from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger

class NewsPage(BasePage):
    def news_button(self):
        news_button = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > label").click()
        