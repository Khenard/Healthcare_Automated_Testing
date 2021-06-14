from controllers import config, login, function_admission, function_oasis, servers, function_snv, patient_dashboard, function_mdo
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
import pyautogui
import subprocess
import autoit

"""

autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("[Class:#32770]", "Button2")"""


todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")

#QA - UNITEST
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/92CE527A-86A2-4386-B1F8-2F853FC06E70/AF19611B-378E-4201-A1B0-A85A454A3576/woundcare/analytics/04BA70D1-12EF-41D0-B8B6-607385AECFFC/4") #QA
time.sleep(5)
edit = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td[2]/button').click()
time.sleep(5)
scrolldown = config.driver.execute_script("window.scrollTo(0,6500);")

fileimage = os.path.abspath("wound.png")


element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="myImg"]'))  # Example xpath
WebDriverWait(config.driver, 10).until(element_present).click() # This opens the windows file selector

#subprocess.Popen('explorer "' + fileimage + '"')


Runtime.getRuntime().exec("C:\\Users\\khena\\Desktop\\FileUpload.exe")



"""pyautogui.write('"' + fileimage + '"') 
time.sleep(5)
pyautogui.press('enter')
"""




"""time.sleep(5)
imageupload = config.driver.find_element_by_xpath('//*[@id="myImg"]')
imageupload.send_keys(fileimage)
"""
print(fileimage)
