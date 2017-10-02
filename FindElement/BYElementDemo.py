from selenium import webdriver
from selenium.webdriver.common.by import By

class ByElementDemo():

    def verifyFindByElement(self):
        sUrl = "http://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(sUrl)

        WebelementById = driver.find_element(By.ID,"name")
        if WebelementById is not None:
                print("verified element by Id using By class  ")


        webElementsByxpath = driver.find_element(By.XPATH,".//*[@id='show-textbox']")
        if webElementsByxpath is not None:
                print("verified the element by xpath using By class")

        WebElementBylinttxt = driver.find_element(By.LINK_TEXT,"Login")

        if WebElementBylinttxt is not None:
            print("verified the By element  by link text using By class ")




        #driver.close()


cc = ByElementDemo()
cc.verifyFindByElement()