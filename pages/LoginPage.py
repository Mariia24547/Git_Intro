from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger
from configs import config


class LoginPage(BasePage):

    email_field = By.CSS_SELECTOR,"[type='email']"
    password_field = By.CSS_SELECTOR,"[type='password']"
    submit_button = By.CSS_SELECTOR, "[type='submit']"

    def login(self,username,password):
        
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        logger.info(f'Entered username={username} and password={password}')
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        logger.info('Clicked on Sign In button')


    def use_login(self,):
        self.login(config.USER,config.USER_PASSWORD)
        #self.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys(config.USER)
        #self.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys(config.USER_PASSWORD)
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        logger.info('Clicked on Sign In button')

    def login_with_blank_username(self):
        self.login(config.USER, config.USER_PASSWORD)
        #self.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys('')
        #self.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys(config.USER_PASSWORD)
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def admin_login(self):
        self.login(config.ADMIN, config.ADMIN_PASSWORD)

        #self.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys('aa')
        #self.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys(config.ADMIN_PASSWORD)
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

