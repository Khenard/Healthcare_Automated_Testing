from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, patient_dashboard, function_woundprocess
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import pyautogui, sys
import autoit

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")

