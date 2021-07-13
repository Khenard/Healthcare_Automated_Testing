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

wound_df = pd.read_excel(datafile, 'wound_assessment')

# Randomize location
col_location = wound_df['LOCATION'].tolist()
location = random.choice(col_location)

# Randomize stages
col_stages = wound_df['STAGES'].tolist()
stages = random.choice(col_stages) # convert to int
stages = str(stages) #convert to string 


# Randomize grantissue
col_grantissue = wound_df['GRANTISSUE'].tolist()
grantissue = int(random.choice(col_grantissue))
grantissue = str(grantissue)

# Randomize nectissue
col_nectissue = wound_df['NECTISSUE'].tolist()
nectissue = int(random.choice(col_nectissue))
nectissue = str(nectissue)

# Randomize granneccoverage
col_granneccoverage = wound_df['GRANNECCOVERAGE'].tolist()
granneccoverage = int(random.choice(col_granneccoverage))
granneccoverage = str(granneccoverage)

# Randomize granneccoverage
col_exuamount = wound_df['EXUAMOUNT'].tolist()
exuamount = int(random.choice(col_exuamount))
exuamount = str(exuamount)

# Randomize exutype
col_exutype = wound_df['EXUTYPE'].tolist()
exutype = random.choice(col_exutype)

# Randomize edges
col_edges = wound_df['EDGES'].tolist()
edges = int(random.choice(col_edges))
edges = str(edges)

# Randomize periwoundtissue
col_periwoundtissue = wound_df['PERIWOUNDTISSUE'].tolist()
periwoundtissue = random.choice(col_periwoundtissue)

# Randomize healingstatus
col_healingstatus = wound_df['HEALINGSTATUS'].tolist()
healingstatus = random.choice(col_healingstatus)

# Randomize woundrelatedpain
col_woundrelatedpain = wound_df['WOUNDRELATEDPAIN'].tolist()
woundrelatedpain = int(random.choice(col_woundrelatedpain))
woundrelatedpain = str(woundrelatedpain)

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

time.sleep(5)

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
function_woundprocess.digitalmeasurement()


# END TEST
 