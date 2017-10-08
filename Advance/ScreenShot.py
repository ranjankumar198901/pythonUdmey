from selenium import webdriver

class ScreenShot():
    def text(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        sspath = "E:\\PythonProjects\\a.png"

        try:
            driver.save_screenshot(sspath)
            print("Screen shot saved --> " + sspath )
        except NotADirectoryError:
            print("not saved ")







cc = ScreenShot()
cc.text()