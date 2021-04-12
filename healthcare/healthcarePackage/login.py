from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

#Configure web driver
chromedriver = os.path.abspath("chromedriver.exe")
driver = webdriver.Chrome(chromedriver)




#Open Chrome and navigate to realtime workflow
driver.maximize_window()
driver.get("https://app.medisource.com/login")

#Set Variables
user_name = "superagent@realtime"
password = "Tester2021!"
submitbtn = driver.find_element_by_xpath("//*[@id='mhLP-ln']/div[2]/form/div[6]/button")


#Get element and applied set variables
element = driver.find_element_by_id("loginemail")
element.send_keys(user_name)
element = driver.find_element_by_id("loginpassword")
element.send_keys(password)
time.sleep(5)
submitbtn.click()




wait = WebDriverWait(driver, 10)
time.sleep(10)
driver.close()