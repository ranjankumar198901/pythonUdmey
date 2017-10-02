from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class findText():

    def textText(self):

        url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(url)

        headertxt = driver.find_element(By.XPATH,"//h1[text()='Practice Page']")
        txt = headertxt.text
        print(txt)
        print("verify the text in the letskodeit site")
        time.sleep(5)

        text2 = driver.find_element(By.XPATH,"//legend[text()='Switch Tab Example']")
        txt2 = text2.text
        print(txt2)

        driver.close()



cc = findText()
cc.textText()