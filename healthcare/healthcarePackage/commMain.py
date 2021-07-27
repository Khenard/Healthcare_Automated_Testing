from controllers import config, login, servers, patient_dashboard
import random, time
from datetime import date
import admission
import functionComm

#import functionRefreshPage
#import screenRecord3

test_server = "qa" # Change the value to qa or live
continuous_test = "yes" # Change the value to yes or no Yes - admitted patient will continue to oasis, no means search existing patients

#screenRecord3.screenRecord()
#admission.admission_medicare(test_server) #PATIENT ADMISSION

servers.qaserver()
time.sleep(7)
config.driver.get("https://qado.medisource.com/patientcare/3477C147-B2D2-449A-AF3D-F5B5FD249BDB/9910164E-A80C-4E10-85CE-C686BEB1866E/overview")

#functionRefreshPage.refresh()
#patient_dahsboard.gettab("communication")
#functionComm.ThirtyDaySummary()

time.sleep(7)
patient_dashboard.gettab("communication") #click niya communication tab
patient_dashboard.newNotes("Communication Notes") #select Communication Notes
time.sleep(7)
functionComm.CommunicationNotesInput()

time.sleep(7)
patient_dashboard.gettab("communication") #click niya communication tab
patient_dashboard.newNotes("HHA Care Plan") #select HHA Care Plan Notes
time.sleep(7)
functionComm.HHAplanInput()


#functionComm.CommunicationTab()
#functionComm.newNotes()
#functionComm.transferSummary()

#functionComm.transferSummaryInput()
#functionComm.CommunicationTab()

#functionComm.newNotes()
#functionComm.dischargeSummary()
#functionComm.dischargeSummaryInput()
#functionRefreshPage.refresh()
#functionComm.CommunicationTab()
#functionComm.newNotes()
#functionComm.DischargeInstructions()
#functionComm.DischargeInstructionsInput()
#functionComm.CommunicationTab()
#functionComm.newNotes()
#functionComm.CaseConference()
#functionComm.CaseConferenceInput()


# COMPLETE SNV TASK
#snv.snv()

# CREATE MDO - PHYSICIAN ORDER
#create_mdo.createmdo()

# END TEST
#config.driver.close()