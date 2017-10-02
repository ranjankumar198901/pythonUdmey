from selenium import webdriver

class launchIE():

    def TestIE(self):
        try:
            surl = "https://letskodeit.teachable.com/p/practice"
            driver = webdriver.Ie('C:\\Users\\ranja\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\IEDriverServer.exe')

            driver.get(surl)
        except Exception as e:
            print(e)


IE = launchIE()
IE.TestIE()