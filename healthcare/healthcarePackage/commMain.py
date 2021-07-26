from controllers import config, login
import random, time
from datetime import date
import admission
import functionComm
#import functionRefreshPage
#import screenRecord3

test_server = "qa" # Change the value to qa or live
continuous_test = "yes" # Change the value to yes or no Yes - admitted patient will continue to oasis, no means search existing patients

#screenRecord3.screenRecord()
admission.admission_medicare(test_server) #PATIENT ADMISSION
#oasis.oasispart() #COMPLETE OASIS SOC
#create_task.create_task(tasks) #CREATE SNV TASK
#functionRefreshPage.refresh()
#functionComm.CommunicationTab()
#functionComm.ThirtyDaySummary()
#functionComm.CommunicationTab()
#functionComm.newNotes()
#functionComm.CommunicationNotes()
#functionComm.CommunicationNotesInput()
#functionComm.CommunicationTab()
#functionComm.newNotes()
#functionComm.HHAplan()

#functionComm.HHAplanInput()
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