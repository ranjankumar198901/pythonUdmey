from selenium import webdriver
import time

class SwitchingWindow():
    def demo(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        print("Successfully launched the browser ")

        #Find the current handle
        parenthandle = driver.current_window_handle
        print("Current window handle is " + parenthandle)
        time.sleep(3)

        #Clicl on open window button
        openwindow = driver.find_element_by_id("openwindow")
        openwindow.click()

        time.sleep(3)
        #Find out all the handles
        all_handles = driver.window_handles
        for a in all_handles:
            print(a)

            if a not in parenthandle:
                driver.switch_to.window(a)
                print("Switched to handle" + a)
                time.sleep(3)
                #Eneter the vlaue in the open browser and click enter
                searchbox   = driver.find_element_by_id("search-courses")
                searchbox.send_keys("Python")
                time.sleep(3)
                break

        #switch back to parent handle
        driver.switch_to.window(parenthandle)
        txtname = driver.find_element_by_id("name")
        txtname.send_keys("Parent window ")






cc = SwitchingWindow()
cc.demo()
