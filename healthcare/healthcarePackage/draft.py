from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo
import ctypes  # An included library with Python install. 


rnskilledassesment = str("RN - Skilled Assessment")
rnskilledassesment_discharge = str("RN - OASIS D1 Discharge from Agency")
rnskilledassesment_recert = str("RN - OASIS D1 Recertification")

oasisdcaegency = str("RN - OASIS D1 Discharge from Agency")
oasisdcnvisit = str("RN - OASIS D1 Discharge Non-visit")
oasisfollowup = str("RN - OASIS D1 Other Follow-Up")
oasistfrfdc = str("RN - OASIS D1 Transfer (discharged)")
oasistfrnotdc = str("RN - OASIS D1 Transfer (not discharged)")
oasisdcsummary = str("RN - Discharge (Summary Only)")
oasisroc = str("RN - OASIS D1 Resumption of Care")

lvnskilledvisit = str("LVN/LPN - Skilled Visit")
lvnwoundvisit = str("LVN/LPN - Wound Visit")
prnskilledvisit = str("PRN - Skilled Visit")
rneducvisit = str("RN - Education Visit")
rnivvisit = str("RN - IV Visit")
rnjschha = str("RN - Joint Supervisory (CHHA)")
rnjslvn = str("RN - Joint Supervisory (LVN)")
rnskilledvisit = str("RN - Skilled Visit")
rnsupvisit = str("RN - Supervisory Visit")
rnwoundvisit = str("RN - Wound Visit")

ptieval = str("PT - Initial Eval")
ptievalsoc = str("PT - Initial Eval-SOC")
ptvisit = str("PT - PT Visit")
ptavisit = str("PTA - PTA Visit")

otieval = str("OT - Initial Eval")
otievalsoc = str("OT - Initial Eval-SOC")
otvisit = str("OT - OT Visit")
otavisit = str("OTA - OTA Visit")

stieval = str("ST - Initial Eval")
stievalsoc = str("ST - Initial Eval-SOC")
stvisit = str("ST - ST Visit")

mswass = str("MSW - Assessment")
mswfollowup = str("MSW - Follow-up Visit")
chhavisit = str("CHHA - HHA Visit")


tasks = [rnivvisit, rnsupvisit, oasistfrnotdc, oasisroc, rnskilledassesment, rnsupvisit, rnskilledassesment] #Enter the task variable you want to create Note: skilledassessment should always the last on the array
rnskilledass = [rnskilledassesment_recert, rnskilledassesment_discharge] # Enter if its recertification or discharge


servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/DBBB3F9A-0D1D-495E-87DC-DAB0CE6B3124/93C9DC38-3BC3-4ACE-ABAC-AA5CB5EB2564/roc-order/BE4933BC-7649-4F40-96EE-B4BA6434B4C8")
time.sleep(2)   


function_complete_task.oasisroc(tasks, "06/29/2021")



#currentpage = config.driver.current_url








# END TEST
 