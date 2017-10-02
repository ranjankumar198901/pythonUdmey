from selenium.webdriver.common.by import By

class HandyWrappers(object):

    def __init__(self,driver):
        self.driver = driver

    def get_By_Type(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID

        elif locatorType == "xpath":
            return By.XPATH

        else:
            print("Locator type not found " + locatorType + " is not correct" )
            return False

    def getElement(self,locator,locatorType):
        element = None

        locatorType = locatorType.lower()
        bytype = self.get_By_Type(locatorType)

        element = self.driver.find_element(bytype,locator)
        print("Element found ")
        return element


