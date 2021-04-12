from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
import time
import os 

chromedriver = os.path.abspath("chromedriver.exe")

#Configure Web Driver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get("https://app.medisource.com/login")

username = driver.find_element_by_id("loginemail")
password = driver.find_element_by_id("loginpassword")
submitbtn = driver.find_element_by_xpath("//*[@id='mhLP-ln']/div[2]/form/div[6]/button")

username.send_keys("superagent@realtime")
time.sleep(2)
password.send_keys("Tester2021!")
time.sleep(5)

submitbtn.click()

driver.execute_script("window.alert('this is an alert');")
time.sleep(5)



wait = WebDriverWait(driver, 10)


driver.close()


"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Configure Web Driver
driver = webdriver.Chrome('C:/Users/jbdor/Downloads/chromedriver_win32/chromedriver.exe')

#Set Variables
user_name = "superagent@realtime"
password = "Tester2021!"

#Open Chrome and navigate to realtime workflow
driver.get("https://app.medisource.com/login")

element = driver.find_element_by_id("loginemail")
element.send_keys(user_name)

element = driver.find_element_by_id("loginpassword")
element.send_keys(password)

element.send_keys(Keys.RETURN)
element.close()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
import time
#Configure Web Driver
driver = webdriver.Chrome('C:/Users/jbdor/Downloads/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.get("https://app.medisource.com/login")

username = driver.find_element_by_id("loginemail")
password = driver.find_element_by_id("loginpassword")
submitbtn = driver.find_element_by_xpath("//*[@id='mhLP-ln']/div[2]/form/div[6]/button")

username.send_keys("superagent@realtime")
time.sleep(2)
password.send_keys("Tester2021!")
time.sleep(5)

submitbtn.click()

driver.execute_script("window.alert('this is an alert');")
time.sleep(5)
alert = driver.switch_to.alert()
alert.accept()


wait = WebDriverWait(driver, 10)


driver.close()





"""




