from selenium import webdriver


class FindByLinkLinkText():

    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://letskodeit.teachable.com/p/practice")
# find element by id
        webelementbyLinktext = driver.find_element_by_link_text("Login")
        if webelementbyLinktext is not None :
            print("successfully verified the link  ")

        webelementPartialLinkTxt = driver.find_element_by_partial_link_text("Sign")

        if webelementPartialLinkTxt is not None:
            print("successfully verified elements by partial Link ")

        driver.close()
ff = FindByLinkLinkText()
ff.test()




