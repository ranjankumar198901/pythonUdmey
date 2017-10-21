from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class javascript():

    def demo(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get("https://www.google.com")

        driver.execute_script("window.location='https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(10)

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

        time.sleep(3)
cc = javascript()
cc.demo()