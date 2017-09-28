from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class dropdownselect:

    def selectvalue(self):
        surl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(surl)

        elem = driver.find_element_by_id("carselect")
        sel = Select(elem)

        sel.select_by_value("benz")
        print("select benz by value")
        time.sleep(5)

        sel.select_by_index("2")
        print("select Honda by value")
        time.sleep(5)

        sel.select_by_visible_text("BMW")
        print("select bmw by value")
        time.sleep(5)

        sel.select_by_index(2)
        print("select honda by value")
        time.sleep(5)

        driver.close()

cc = dropdownselect()
cc.selectvalue()