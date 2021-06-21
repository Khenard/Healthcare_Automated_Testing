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


tasks = [rnwoundvisit, rnivvisit] #Enter the task variable you want to create

servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/E2B75EF7-0338-48A6-861A-629BADEB0008/BE8D6183-82BC-4C73-ABC2-3677C533C333/overview")
time.sleep(2)   


create_task.create_task(tasks)








# END TEST
 