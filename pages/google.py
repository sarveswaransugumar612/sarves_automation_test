from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Google_class:

    def __init__(self,driver):
        self.driver = driver

    def search_text(self,text):
        self.driver.find_element(By.NAME, 'q').send_keys(text)
        self.driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
        time.sleep(5)


