from selenium import webdriver


class findByxpathCss():

    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://letskodeit.teachable.com/p/practice")
# find element by xpath
        webelementByXpath = driver.find_element_by_xpath(".//*[@id='name']")

        if webelementByXpath is not None :
            print("successfully verified element By xpath ")

        webelementCss = driver.find_element_by_css_selector("#displayed-text")

        if webelementCss is not None:
            print("successfully verified elements by Css")

        driver.close()
ff = findByxpathCss()
ff.test()




