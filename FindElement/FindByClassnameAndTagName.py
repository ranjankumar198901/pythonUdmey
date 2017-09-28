from selenium import webdriver


class FindByClassnameAndTagName():

    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://letskodeit.teachable.com/p/practice")
# find element by id
        webelementbyClassName = driver.find_element_by_class_name("inputs")
        if webelementbyClassName is not None :
            print("successfully verified the Class Name ")

        webelementTagName = driver.find_element_by_tag_name("a")

        if webelementTagName is not None:
            print("successfully verified elements by Tag Name ")

        driver.close()
ff = FindByClassnameAndTagName()
ff.test()




