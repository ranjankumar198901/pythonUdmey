from selenium import webdriver
import time

class HiddenElement():

    def TestHiddenElement(self):
        try:
            url = "https://letskodeit.teachable.com/p/practice"
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(url)

            showBtnelement  = driver.find_elements_by_id("show-textbox")
            hideBtn = driver.find_element_by_id("hide-textbox")
            showHideTestBox = driver.find_element_by_xpath("//input[@id='displayed-text']")

            showBtnelement.c

            print("all element is present ")


        except Exception as e :
            print("this is Except block and the exception is " + e)
        finally:
            print("this is finally block ")








        #Close Browser
        #driver.close()




cc = HiddenElement()
cc.TestHiddenElement()



