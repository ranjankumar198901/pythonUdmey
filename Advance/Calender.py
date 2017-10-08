from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class selectCalender():

    def testCalender(self):

        surl = "https://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(surl)
        driver.implicitly_wait(3)

        flightElement = driver.find_element(By.XPATH,"//a[@id='tab-flight-tab']")
        flightElement.click()

        time.sleep(3)

        departCal = driver.find_element(By.XPATH,"//input[@id='flight-departing']")
        departCal.click()

        finddate = driver.find_element(By.XPATH,"//div[@class='datepicker-cal-month'][position()=1]//button[text()='9']")
        finddate.click()

        time.sleep(3)
        print("successsfully clicked on the given date")




cc = selectCalender()
cc.testCalender()

