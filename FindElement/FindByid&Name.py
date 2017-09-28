from selenium import webdriver


class findElement():

    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://letskodeit.teachable.com/p/practice")
# find element by id
        webelement_id = driver.find_element_by_id("openwindow")
        if webelement_id is not None :
            print("successfully verified id ")

        webelement_name = driver.find_element_by_name("enter-name")

        if webelement_name is not None:
            print("successfully verified elements by name")

        driver.close()
ff = findElement()
ff.test()




