from controllers import config, login, function_admission, function_oasis, servers
import random, time
from datetime import date
import admission, oasis, create_task, snv


test_server = "live" # Change the value to qa or live
continuous_test = "yes" # Change the value to yes or no Yes - admitted patient will continue to oasis, no means search existing patients

if test_server == "qa":
    servers.qaserver()
    config.driver.get("https://qado.medisource.com/patient") #Navigate to Add patient page
elif test_server == "live":
    servers.liveserver()
    config.driver.get("https://app.medisource.com/patient") #Navigate to Add patient page


admission.admission(test_server)

oasis.oasis(test_server, continuous_test)

create_task.create_task(test_server, continuous_test)

snv.snv(test_server, continuous_test)

config.driver.close()