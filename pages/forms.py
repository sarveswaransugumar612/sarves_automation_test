from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
first_name_element_id = "firstname"
last_name_id = "lasttname"

class form_class:

    def __init__(self,driver):
        self.driver = driver

    def enter_first_name(self,fname,lname):
        self.driver.find_element(By.ID,first_name_element_id).send_keys(fname)
        self.driver.find_element(By.ID,first_name_element_id).send_keys(lname)






