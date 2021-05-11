import config, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import login

# ------------------------------------------------------------------------------------------------
#  REDIRECTION
# ------------------------------------------------------------------------------------------------
config.driver.maximize_window()
config.driver.get("https://qado.medisource.com/login")

# ------------------------------------------------------------------------------------------------
#  LOGIN
# ------------------------------------------------------------------------------------------------
login.login("superagent@unitest", "Tester2021@")
time.sleep(2)
config.driver.get("https://qado.medisource.com/patientcare/6AC5254A-5F58-4162-8A64-4B7B749BCA3E/190ABC8F-75B0-49F7-BAC2-06A43EC9ACCF/overview")
time.sleep(5)

