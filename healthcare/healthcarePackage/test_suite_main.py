import config
import login, admit_patient

#Open Chrome and navigate to realtime workflow
config.driver.maximize_window()
config.driver.get("https://qado.medisource.com/login")

#login function
login.login("superagent@unitest", "Tester2021!")

#admission patient
admit_patient.admission(
    "01/01/2021",
    "1200",
    "01/01/2021",
    "Automated",
    "Patient",
    "M",
    "Jr.",
    "02/07/1997",
    "Male",
    "Single",
    "American", 
    "english",
    "500000000",
    "17 Peachtree St, Charleston, MS, 38921",
    "Blue Building",
    "17 Peachtree St",
    "Charleston",
    "MS",
    "38921",
    "8593603818",
    "6626472513",
    "automatedpatient@mailinator.com",
    "Ken Figuracion",
    "8593603818",
    "Catherine Balanag",
    "Wife",
    "8593603818",
    "6626472513",
    "01/01/2018",
    "02/01/2018",
    "Colon and Rectal Surgery",
    "Peanut",
    "RN"
    )





