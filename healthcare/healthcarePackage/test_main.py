from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard
import random, time
from datetime import date
import admission, oasis, create_task, snv, create_mdo

test_server = "qa" # Change the value to qa or live
continuous_test = "yes" # Change the value to yes or no Yes - admitted patient will continue to oasis, no means search existing patients

# PATIENT ADMISSION
admission.admission(test_server)

# COMPLETE OASIS SOC
oasis.oasis(test_server, continuous_test)

# CREATE SNV TASK
create_task.create_task(test_server, continuous_test)

# COMPLETE SNV TASK
snv.snv()

# CREATE MDO - PHYSICIAN ORDER
create_mdo.createmdo()

# END TEST
config.driver.execute_script('alert("Test Successful!");')
config.driver.close()