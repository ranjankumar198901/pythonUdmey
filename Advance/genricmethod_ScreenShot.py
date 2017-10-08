from selenium import webdriver
import time
class genricmethod_ScreenShot():
    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        self.takeScreenShot(driver)

    def takeScreenShot(self,driver):

        ssname = str(round(time.time() * 1000)) +".png"
        screenshotdir = "E:\\PythonProjects\\" + ssname

        try:
            driver.save_screenshot(screenshotdir)
            print("Screen shot saved --> " + screenshotdir )
        except NotADirectoryError:
            print("not saved ")

cc = genricmethod_ScreenShot()
cc.test()