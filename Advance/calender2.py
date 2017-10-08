from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class calender2:

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.expedia.co.in")
        driver.implicitly_wait(4)

        #Click on Flight Tab
        flightTab = driver.find_element(By.XPATH,"//a[@id='tab-flight-tab']")
        flightTab.click()

        time.sleep(5)

        #Click on flight Departure text box
        departingtxt = driver.find_element(By.XPATH,"//input[@id='flight-departing']")
        departingtxt.click()
        time.sleep(2)
       # if driver.find_element(By.XPATH,"//div[@class='datepicker-cal-month'][position()=1]") is True:
        #    print("the date picker is diaplayed ")
        pickedDt = driver.find_element(By.XPATH,"//div[@class='datepicker-cal-month'][position()=1]//button[text()='9']")
        pickedDt.click()

        time.sleep(10)

        departingtxt.click()
        dateList = driver.find_elements(By.XPATH,"//div[@class='datepicker-cal-month'][position()=1]//button[@class ='datepicker-cal-date']")

        for dt in dateList:
            if dt.text == "10":
                dt.click()
                print("Clicked the date" )
                break

        time.sleep(5)
cc = calender2()
cc.test()