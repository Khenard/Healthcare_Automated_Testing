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

# Declare as variable the data xlsx file - put it on the same folder as the project
datafile = os.getcwd()+"\data.xlsx" 
# Declare excel data as variable and set the first column to ID
excel_data = pd.read_excel(datafile)
#age = pd.DataFrame(excel_data, columns =['NAME'])
#convert column data to array list and use it to select random values
col_name = excel_data['NAME'].tolist()
print(col_name)
name_random = random.choice(col_name)
    
wound_df = pd.read_excel(datafile, 'wound_assessment')

# Randomize location
col_location = wound_df['LOCATION'].tolist()
location = random.choice(col_location)

# Randomize stages
col_stages = wound_df['STAGES'].tolist()
stages = int(random.choice(col_stages))

# Randomize grantissue
col_grantissue = wound_df['GRANTISSUE'].tolist()
grantissue = int(random.choice(col_grantissue))

# Randomize nectissue
col_nectissue = wound_df['NECTISSUE'].tolist()
nectissue = int(random.choice(col_nectissue))

# Randomize granneccoverage
col_granneccoverage = wound_df['GRANNECCOVERAGE'].tolist()
granneccoverage = int(random.choice(col_granneccoverage))

# Randomize granneccoverage
col_exuamount = wound_df['EXUAMOUNT'].tolist()
exuamount = int(random.choice(col_exuamount))





print(location)
print(stages)
print(grantissue)
print(nectissue) 
print(granneccoverage)
print(exuamount) 
print(exutype)
print(edges) 
print(periwoundtissue)
print(healingstatus) 
print(woundrelatedpain) 

    
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/CEB7010B-2FE7-45B1-808C-3C25C0E594F0/857A6F1E-C5A3-415E-92FC-879D983FAA2F/woundcare/update/435CC653-F0D9-4E4A-96C2-C16763973186/1")



    

function_woundprocess.completewoundassessment(
    stages, 
    grantissue, 
    nectissue, 
    granneccoverage, 
    exuamount, 
    exutype, 
    edges, 
    periwoundtissue,
    healingstatus, 
    woundrelatedpain
    )
    



# END TEST
 