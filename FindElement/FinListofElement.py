from selenium import webdriver
from selenium.webdriver.common.by import By

class FindListofElement():

    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://letskodeit.teachable.com/p/practice")
    # find list of element in the page using find_elements_by_class_name
        webelementlistByClassname = driver.find_elements_by_class_name("inputs")
        lenget1 = len(webelementlistByClassname)
        if webelementlistByClassname is not None :
            print("successfully verified the list of Class Name " + str(lenget1))

    # using find_Elements  Yet to ses
        webelementlistByClassname2 = driver.find_elements(By.CLASS_NAME,"inputs")
        lenget2 = len(webelementlistByClassname2)
        if webelementlistByClassname2 is not None:
            print("successfully verified the list of Class Name " + str(lenget2))

        driver.close()
ff = FindListofElement()
ff.test()




