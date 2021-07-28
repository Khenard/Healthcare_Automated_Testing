from controllers import config, login, servers, patient_dashboard
import random, time
from datetime import date
import admission
import functionComm


test_server = "qa" # Change the value to qa or live
continuous_test = "yes" # Change the value to yes or no Yes - admitted patient will continue to oasis, no means search existing patients



admission.admission_medicare(test_server) #PATIENT ADMISSION
#servers.qaserver()
#config.driver.get("https://qado.medisource.com/patientcare/3477C147-B2D2-449A-AF3D-F5B5FD249BDB/9910164E-A80C-4E10-85CE-C686BEB1866E/overview")

time.sleep(5)

patient_dashboard.gettab("communication")
time.sleep(5)
functionComm.ThirtyDaySummary()

time.sleep(5)
patient_dashboard.gettab("communication") #click niya communication tab
patient_dashboard.newNotes("Communication Notes") #select Communication Notes
time.sleep(5)
functionComm.CommunicationNotesInput()

time.sleep(5)
patient_dashboard.gettab("communication") #click niya communication tab
patient_dashboard.newNotes("HHA Care Plan") #select HHA Care Plan Notes
time.sleep(5)
functionComm.HHAplanInput()

time.sleep(5)
patient_dashboard.gettab("communication") #click niya communication tab
patient_dashboard.newNotes("Transfer Summary") #select Transfer Summary
time.sleep(5)
functionComm.transferSummaryInput()

time.sleep(5)
patient_dashboard.gettab("communication") #click niya communication tab
patient_dashboard.newNotes("Discharge Summary") #select Discharge Summary
time.sleep(5)
functionComm.dischargeSummaryInput()

time.sleep(5)
patient_dashboard.gettab("communication") #click niya communication tab
patient_dashboard.newNotes("Discharge Instruction") #select Discharge Instruction
time.sleep(5)
functionComm.DischargeInstructionsInput()
dcbutton = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[1]').click()
time.sleep(2)
dcyes = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()

time.sleep(5)
patient_dashboard.gettab("communication") #click niya communication tab
patient_dashboard.newNotes("Case Conference") #select Case Conference
time.sleep(5)
functionComm.CaseConferenceInput()



# END TEST
config.driver.close()