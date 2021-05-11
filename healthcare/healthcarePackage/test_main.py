from controllers import config, login, function_admission, function_oasis, servers
import random, time
from datetime import date
import admission, oasis, create_task

test_server = "qa"

if test_server == "qa":
    servers.qaserver()
    config.driver.get("https://qado.medisource.com/patient") #Navigate to Add patient page
elif test_server == "live":
    servers.liveserver()
    config.driver.get("https://app.medisource.com/patient") #Navigate to Add patient page
    
admission.admission()

oasis.oasis(test_server)


config.driver.close()