from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_create_task, function_complete_task
import random, time
from datetime import date
import admission, oasis, create_task, complete_task, create_mdo, complete_woundprocess
import pymsgbox


rnskilledassesment = "RN - Skilled Assessment"
rnskilledassesment_dc = "RN - OASIS D1 Discharge from Agency"
rnskilledassesment_recert = "RN - OASIS D1 Recertification"

oasisdcnvisit = "RN - OASIS D1 Discharge Non-visit"
oasisfollowup = "RN - OASIS D1 Other Follow-Up"
oasistfrfdc = "RN - OASIS D1 Transfer (discharged)"
oasistfrnotdc = "RN - OASIS D1 Transfer (not discharged)"
oasisdcsummary = "RN - Discharge (Summary Only)"
oasisroc = "RN - OASIS D1 Resumption of Care"

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


rnskilledassesment = "RN - Skilled Assessment"
rnskilledassesment_dc = "RN - OASIS D1 Discharge from Agency"
rnskilledassesment_recert = "RN - OASIS D1 Recertification"

oasisdcaegency = "RN - OASIS D1 Discharge from Agency"
oasisdcnvisit = "RN - OASIS D1 Discharge Non-visit"
oasisfollowup = "RN - OASIS D1 Other Follow-Up"
oasistfrfdc = "RN - OASIS D1 Transfer (discharged)"
oasistfrnotdc = "RN - OASIS D1 Transfer (not discharged)"
oasisdcsummary = "RN - Discharge (Summary Only)"
oasisroc = "RN - OASIS D1 Resumption of Care"

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


def test_main(servertest):
    
    test_server = servertest # Change the value to qa or live
    
    #Enter the task variable you want to create Note: skilledassessment should always the last on the array
    tasks = [rnivvisit, rnsupvisit, oasistfrnotdc, oasisroc, rnskilledassesment, rnsupvisit, rnskilledassesment] 
    rnskilledass = [rnskilledassesment_recert, rnskilledassesment_dc] # Enter if its recertification or discharge

    #tasks = [rnivvisit, rnsupvisit, oasistfrnotdc, oasisroc, rnskilledassesment, rnsupvisit, rnskilledassesment, rnskilledassesment] #Enter the task variable you want to create Note: skilledassessment should always the last on the array
    #rnskilledass = [rnskilledassesment_recert, rnskilledassesment_dc, rnskilledassesment_recert] # Enter if its recertification or discharge
   
    admission.admission_medicare(test_server) #PATIENT ADMISSION
    oasis.oasispart() #COMPLETE OASIS SOC
    create_task.create_task(tasks, rnskilledass)
    
    pymsgbox.alert('Test Success!', 'Success')
    print('Test success!')   
    config.driver.close()
    

def preadmitpatient_medicare(servertest):
    
    test_server = servertest 
    admission.preadmission_medicare(test_server) #PATIENT ADMISSION
    
    if servertest == "qa":
        config.driver.get("https://qado.medisource.com/patients/pre-admitted")
    elif servertest == "live": 
        config.driver.get("https://app.medisource.com/patients/pre-admitted")
    
    pymsgbox.alert('Test Success!', 'Success')
    print('Test success!')   
    config.driver.close()

def preadmitpatient_nonmedicare(servertest):
    
    test_server = servertest 
    admission.preadmission_nonmedicare(test_server) #PATIENT ADMISSION
    
    if servertest == "qa":
        config.driver.get("https://qado.medisource.com/patients/pre-admitted")
    elif servertest == "live": 
        config.driver.get("https://app.medisource.com/patients/pre-admitted")
        
    pymsgbox.alert('Test Success!', 'Success')
    print('Test success!')   
    config.driver.close()
    
def wound(servertest, searchpatient):
    test_server = servertest 
    complete_woundprocess.complete_woundprocess(servertest, searchpatient)
    
    print('Test success!')   
    pymsgbox.alert('Test Success!', 'Success')
    print('Test success!')   
    config.driver.close()
    
    
    
    
    
    
    
    
    
    

