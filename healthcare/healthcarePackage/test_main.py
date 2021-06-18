from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_create_task
import random, time
from datetime import date
import admission, oasis, create_task, snv, create_mdo


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
tasks = [prnskilledvisit, rnivvisit, rnsupvisit]




test_server = "qa" # Change the value to qa or live
continuous_test = "yes" # Change the value to yes or no Yes - admitted patient will continue to oasis, no means search existing patients

# PATIENT ADMISSION
admission.admission(test_server)

# COMPLETE OASIS SOC
oasis.oasispart()

# CREATE SNV TASK
create_task.create_task(tasks)





# COMPLETE SNV TASK
#snv.snv()

# CREATE MDO - PHYSICIAN ORDER
#create_mdo.createmdo()

# END TEST
config.driver.close()