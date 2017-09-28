from selenium import webdriver

import time

class BrowserInteraction():

    def testBrowser(self):
        try:
            surl= "https://letskodeit.teachable.com/p/practice"
            driver = webdriver.Chrome()
            driver.get(surl)

        #Window maximaze
            driver.maximize_window()

        #Window Title
            Title_window = driver.title
            print("Browser title is " + Title_window )

        # Current URL
            scurrentURL = driver.current_url
            print(" current url of the page is " + scurrentURL )

        #Refresh
            driver.refresh()

        #Refersh current page  / 2nd way to refresh the page
            driver.get(driver.current_url)

        #open another url
            driver.get("https://www.google.co.in")

        #Back
            driver.back()

        #Forward
            driver.forward()

        #Page source
            spagesrc = driver.page_source
            print( "The page source is " + spagesrc)


        #Close
        #driver.close()

        #Quit
        #driver.quit()
            driver.close()

        except:
            print("in the exception block")

        finally:
            print("this is a fianlly bolck ")


testBrowserElement = BrowserInteraction()
testBrowserElement.testBrowser()