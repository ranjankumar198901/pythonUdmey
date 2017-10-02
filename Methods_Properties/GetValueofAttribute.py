from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetValueofAttribute():

    def testAttribute(self):

        url = ""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")


        element = driver.find_element(By.ID,"name")
        Result = element.get_attribute("class")
        Result2 = element.get_attribute("placeholder")

        print("the value of the attibute is " + Result +"  "+ Result2)

        driver.close()


cc = GetValueofAttribute()
cc.testAttribute()