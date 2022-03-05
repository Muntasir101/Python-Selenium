'''
Created on May 30, 2018
@author: venkateshwara.d
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class Screenshots():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        chrome_driver_path = os.path.abspath('..')  + "\\Drivers\\chromedriver.exe"
 
        driver=webdriver.Chrome(chrome_driver_path)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        destinationFileName = "/Users/atomar/Desktop/test.png" # Mac
        # destinationFileName = "C:\\atomar\\Desktop" -> Windows

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()
