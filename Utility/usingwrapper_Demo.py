from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Utility.handywrapper import HandyWrappers

class usingwrapper_Demo:

    def test(self):
        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        time.sleep(5)
        hw = HandyWrappers(driver)

        elementtxtbox = hw.getElement("name","id")
        elementtxtbox.send_keys("hi")


cc = usingwrapper_Demo()
cc.test()