# from urllib import req

import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def config(request):
    driver = webdriver.Chrome()
    driver.get("https://letcode.in/forms")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    driver.close()