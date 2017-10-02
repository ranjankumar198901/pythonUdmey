from selenium import webdriver


class launchbrowser():

    def tesBrowser_Launch(self):
        try:

            url = "https://letskodeit.teachable.com/p/practice"
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(url)
        except Exception as e:
            print(e)

FF = launchbrowser()
FF.tesBrowser_Launch()

