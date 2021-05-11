import random, time
from datetime import date
from controllers import config, login, function_admission, function_oasis, servers
import admission, oasis, create_task

#--------------------------------------------------------------------------------------------
#  SELECT SERVER FOR TEST
# ------------------------------------------------------------------------------------------------

servers.qaserver() #QA server
config.driver.get("https://qado.medisource.com/patient") #Navigate to Add patient page

#servers.liveserver() #Live server
#config.driver.get("https://app.medisource.com/patient") #Navigate to Add patient page

# ------------------------------------------------------------------------------------------------
admission.admission()

# ------------------------------------------------------------------------------------------------
oasis.oasis()


config.driver.close()