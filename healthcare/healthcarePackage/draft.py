from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_woundprocess
import time, random
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo, complete_woundprocess
import ctypes
import pyautogui, sys
import autoit
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


servers.liveserver()
config.driver.get("https://app.medisource.com/patientcare/AAC52220-34A4-4AFE-B558-B3B03E86AA3B/3EC4BC54-95AE-464A-B76D-9FE369404133/2020/oasis/soc/027D46A6-0B09-4255-A16B-FC2F09CC5FCE/AAC52220-34A4-4AFE-B558-B3B03E86AA3B/v3/clinical")
time.sleep(5)
config.take_screenshot()
config.take_video()

# END TEST
 