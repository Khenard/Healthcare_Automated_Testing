from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_create_task
import random, time
from datetime import date
import admission, oasis, create_task, snv, create_mdo

test_server = "live" # Change the value to qa or live
continuous_test = "yes" # Change the value to yes or no Yes - admitted patient will continue to oasis, no means search existing patients

# PATIENT ADMISSION
#admission.admission(test_server)

servers.liveserver()
# COMPLETE OASIS SOC
#oasis.oasis()
config.driver.get("https://app.medisource.com/patientcare/72B2B9EA-305C-4C2D-9EEE-B7F8F453E5B9/BC5039E4-EB8E-4C00-879E-2A7F2012352E/overview")
time.sleep(3)

# CREATE SNV TASK
create_task.create_task()

# COMPLETE SNV TASK
snv.snv()

# CREATE MDO - PHYSICIAN ORDER
create_mdo.createmdo()

# END TEST
config.driver.close()