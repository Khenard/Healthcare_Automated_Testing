from controllers import config, login, servers, creatTask
import random, time
from datetime import date
import admission
import functionComm
from datetime import date
from datetime import datetime, timedelta



test_server = "qa" # Change the value to qa or live
continuous_test = "yes" # Change the value to yes or no Yes - admitted patient will continue to oasis, no means search existing patients

#screenRecord3.screenRecord()
#admission.admission(test_server) #PATIENT ADMISSION
servers.qaserver()
config.driver.get("https://qado.medisource.com/patientcare/0D07C17E-2DB5-460F-AABC-1A051DA5FCF1/DB98F712-6EF7-4158-A606-461D4D696B8D/overview")
time.sleep(7)
 
#createTask
creatTask.lvnSV()
time.sleep(7)

creatTask.lvnWV()
time.sleep(7)

creatTask.prnSV()
time.sleep(7)

creatTask.rnEV()
time.sleep(7)

creatTask.rnIV()
time.sleep(7)

creatTask.rnJSHHA()
time.sleep(7)

creatTask.rnJSLVN()
time.sleep(7)


creatTask.rnSV()
time.sleep(7)

creatTask.rnSupV()
time.sleep(7)

creatTask.rnWV()
time.sleep(7)

creatTask.ptIE()
time.sleep(7)

creatTask.stIE()
time.sleep(7)

creatTask.otIE()
time.sleep(7)

creatTask.mswa()
time.sleep(7)

creatTask.mswfv()
time.sleep(7)

creatTask.chha()
time.sleep(7)


# END TEST
config.driver.close()