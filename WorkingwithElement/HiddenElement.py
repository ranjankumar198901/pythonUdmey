from selenium import webdriver
import time

class HiddenElement():
    def TestHiddenElement(self,):
        try:
            url = "https://letskodeit.teachable.com/p/practice"
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(url)
            time.sleep(5)

            showBtnelement  = driver.find_element_by_id("show-textbox")
            hideBtn = driver.find_element_by_id("hide-textbox")
            showHideTestBox = driver.find_element_by_xpath("//input[@id='displayed-text']")

            state_textBox = showHideTestBox.is_displayed()
            print(" the state of the text box is " + str(state_textBox))

            # Click on hide Button
            hideBtn.click()
            print("click on hide Buttom")
            time.sleep(2)

           #Find the sate of the text box
            state_textBox = showHideTestBox.is_displayed()
            print(" the state of the text box is " + str(state_textBox) )

           # Click on show button
            showBtnelement.click()

            # find the state of the text box
            state_textBox = showHideTestBox.is_displayed()

            print(" the state of the text box is " + str(state_textBox))

           # Browser Close
            driver.close()


        except Exception as e:
            print("this is Except block and the exception is " + str(e))
        #finally:
         #   print("this is finally block ")
#----------------------------------------------------------------------------------

    def TestExpedia(self):
        driver2 = webdriver.Chrome()
        driver2.maximize_window()
        driver2.get("https://www.expedia.com")

        driver2.find_element_by_id("tab-flight-tab").click()

        AgeElement = driver2.find_element_by_id("hotel-1-age-select-1")
        print("Age is displayed " + str(AgeElement.is_displayed()))

        driver2.close()
    


cc = HiddenElement()
cc.TestHiddenElement()

cc.TestExpedia()

