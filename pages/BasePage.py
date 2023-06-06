from selenium.webdriver.common.by import By


class BasePage:


    TIMEOUT = 15
    def __init__(self,driver) -> None:
        self.driver = driver

    
        