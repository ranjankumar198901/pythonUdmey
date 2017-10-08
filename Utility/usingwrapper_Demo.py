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

        elementtxtbox1 = hw.getElement("name","id")
        elementtxtbox1.send_keys("test")

        time.sleep(5)

        elementtxtbox2 =hw.getElement("//input[@id='name']","xpath")
        elementtxtbox2.clear()
        print("successfully cleared the text box")




cc = usingwrapper_Demo()
cc.test()