from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException
import pymsgbox
from datetime import date

# Useful variables from config.py
todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
name_random = config.randomize_name()
ssn = config.randomize_ssn()
today = date.today()
todaynow = today.strftime("%m/%d/%Y")   

taskdateconvert = datetime.strptime(todaynow, '%m/%d/%Y') #2. Convert to date string
addeddaystodate = timedelta(days=1000) #3. Add days to the date
datetotal = taskdateconvert + addeddaystodate #4. add total
finaltaskdate = datetime.strftime(datetotal, '%m/%d/%Y') #5. convert again to date string for final date  
print(finaltaskdate)



