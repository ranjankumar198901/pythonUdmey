from selenium import webdriver
from selenium.webdriver.common.by import By
import  time


class airbnb_Exercice():

    def testsirbnb(self):

        url = ""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.airbnb.co.in/")

        element = driver.find_element_by_xpath("//input[@id='GeocompleteController-via-SearchBarLarge-via-HeroController']")
        element.send_keys("New Delhi")

        search_Btn = driver.find_element(By.XPATH,"//button[@class='_vuq6rr']")
        search_Btn.click()

        time.sleep(5)
        verifytxt = driver.find_element(By.XPATH,"//h3[contains(text(),'Explore New Delhi')]")
        if verifytxt.is_displayed() is True:
            print("successfully verified the home page" + str(verifytxt.text) )

        time.sleep(5)

        driver.close()




cc = airbnb_Exercice()
cc.testsirbnb()