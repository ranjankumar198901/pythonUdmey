from selenium import webdriver
import time
class AutoComplete():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.southwest.com/")
        driver.implicitly_wait(4)

        departuretxt = driver.find_element_by_id("air-city-departure")
        departuretxt.send_keys("New York")
        time.sleep(5)
        driver.find_element_by_xpath("//ul[@id='air-city-departure-menu']//li[contains(text(),'/Newark, NJ - EWR')]").click()
        print("Clicked in New york EWR")

cc = AutoComplete()
cc.test()