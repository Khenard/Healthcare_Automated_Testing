from controllers import config, login, function_admission, function_oasis, servers, function_snv, function_create_task, patient_dashboard, function_mdo
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait

rnskilledassesment = "RN - Skilled Assessment"
oasisdcaegency = "RN - OASIS D1 Discharge from Agency"
oasisdcnvisit = "RN - OASIS D1 Discharge Non-visit"
oasisfollowup = "RN - OASIS D1 Other Follow-Up"
oasistfrfdc = "RN - OASIS D1 Transfer (discharged)"
oasistfrnotdc = "RN - OASIS D1 Transfer (not discharged)"

lvnskilledvisit = "LVN/LPN - Skilled Visit"
lvnwoundvisit = "LVN/LPN - Wound Visit"
prnskilledvisit = "PRN - Skilled Visit"
rneducvisit = "RN - Education Visit"
rnivvisit = "RN - IV Visit"
rnjschha = "RN - Joint Supervisory (CHHA)"
rnjslvn = "RN - Joint Supervisory (LVN)"
rnskilledvisit = "RN - Skilled Visit"
rnsupvisit = "RN - Supervisory Visit"
rnwoundvisit = "RN - Wound Visit"
ptieval = "PT - Initial Eval"
ptievalsoc = "PT - Initial Eval-SOC"
ptvisit = "PT - PT Visit"
ptavisit = "PTA - PTA Visit"
otieval = "OT - Initial Eval"
otievalsoc = "OT - Initial Eval-SOC"
otvisit = "OT - OT Visit"
otavisit = "OTA - OTA Visit"
stieval = "ST - Initial Eval"
stievalsoc = "ST - Initial Eval-SOC"
stvisit = "ST - ST Visit"
mswass = "MSW - Assessment"
mswfollowup = "MSW - Follow-up Visit"
chhavisit = "CHHA - HHA Visit"


#Enter the task variable you want to create
tasks = [mswass, rnivvisit, lvnskilledvisit, lvnwoundvisit, rnivvisit, prnskilledvisit, ptieval]


servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/4A69A4F8-11F6-489E-9349-543B714443E4/7EC38970-4B43-4AF6-A456-89870347EDF1/overview")
   

# CREATE SNV TASK
create_task.create_task(tasks)



# END TEST
