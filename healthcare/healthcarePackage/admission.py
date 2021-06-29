from controllers import config, function_admission, function_oasis, servers
import random, time
from datetime import date
from datetime import datetime, timedelta
import oasis

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
    
def admission_medicare(test_server):
    
    if test_server == "qa":
        servers.qaserver()
        config.driver.get("https://qado.medisource.com/patient") #QA
        time.sleep(2)
    elif test_server == "live":
        servers.liveserver()
        config.driver.get("https://app.medisource.com/patient") #LIVE
        time.sleep(2)
    
    today = date.today()
    todaynow = today.strftime("%m/%d/%Y")
    
    #random number for patient name and SSN 
    name_random = ["Leonel", "Juana", "Deandra", "Jazmin", "Keila", "Claudine", "Kathleen", "Sandra", "Yael", "Frieda", "Emile", "Dane", "Carmella", "Rosalva", "Denita", "Marvis", "Vilma", "Lucila", "Coral", "James", "Jerald", "Buford", "Vennie"  
                   "Cathy", "Melody", "Siobhan", "Annmarie", "Tanna", "Liliana", "Keshia", "Irwin", "Jacqualine", "Leigh", "Sulema", "Marty", "Mike", "Shonta", "Lane", "Eldora", "Adah", "Leland", "Teresia", "Chloe", "Cordie", "Hal", "Sherryl", "Reggie", "Chery", "Columbus", "Edith"]
    
    pn = random.choice(name_random)
    ssn = random.randint(0, 9999999999)
    
    # ------------------------------------------------------------------------------------------------
    #  PATIENT ADMISSION
    # ------------------------------------------------------------------------------------------------

    #admission patient
    function_admission.admission(
        todaynow,
        todaytime,
        todaynow,
        str(pn),
        "Automated",
        str(pn),
        "02/07/1997",
        "Male",
        "Single",
        "American", 
        "english",
        ssn,
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
    
    #This function is to get the current browser url to get the link of the current patient dashboard
    #getlastpatient = config.driver.get(config.driver.current_url)
    getlastpatient = config.driver.current_url
    
    #oasis.getpatientlink(getlastpatient)
     
    time.sleep(5)
   
   

def preadmission_medicare(test_server):
    
    if test_server == "qa":
        servers.qaserver()
        config.driver.get("https://qado.medisource.com/patient") #QA
        time.sleep(2)
    elif test_server == "live":
        servers.liveserver()
        config.driver.get("https://app.medisource.com/patient") #LIVE
        time.sleep(2)
    
    today = date.today()
    todaynow = today.strftime("%m/%d/%Y")
    
    #random number for patient name and SSN 
    name_random = ["Leonel", "Juana", "Deandra", "Jazmin", "Keila", "Claudine", "Kathleen", "Sandra", "Yael", "Frieda", "Emile", "Dane", "Carmella", "Rosalva", "Denita", "Marvis", "Vilma", "Lucila", "Coral", "James", "Jerald", "Buford", "Vennie"  
                   "Cathy", "Melody", "Siobhan", "Annmarie", "Tanna", "Liliana", "Keshia", "Irwin", "Jacqualine", "Leigh", "Sulema", "Marty", "Mike", "Shonta", "Lane", "Eldora", "Adah", "Leland", "Teresia", "Chloe", "Cordie", "Hal", "Sherryl", "Reggie", "Chery", "Columbus", "Edith"]
    
    pn = random.choice(name_random)
    ssn = random.randint(0, 9999999999)
    
    # ------------------------------------------------------------------------------------------------
    #  PATIENT ADMISSION
    # ------------------------------------------------------------------------------------------------

    #admission patient
    function_admission.preadmission_med(
        todaynow,
        todaytime,
        str(pn),
        "Automated M",
        str(pn),
        "02/07/1997",
        "Male",
        "Single",
        "American", 
        "english",
        ssn,
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
    
    #This function is to get the current browser url to get the link of the current patient dashboard
    #getlastpatient = config.driver.get(config.driver.current_url)
    getlastpatient = config.driver.current_url
    
    #oasis.getpatientlink(getlastpatient)
    
    time.sleep(5)
    



def preadmission_nonmedicare(test_server):
    
    if test_server == "qa":
        servers.qaserver()
        config.driver.get("https://qado.medisource.com/patient") #QA
        time.sleep(2)
    elif test_server == "live":
        servers.liveserver()
        config.driver.get("https://app.medisource.com/patient") #LIVE
        time.sleep(2)
    
    today = date.today()
    todaynow = today.strftime("%m/%d/%Y")
    
    #random number for patient name and SSN 
    name_random = ["Leonel", "Juana", "Deandra", "Jazmin", "Keila", "Claudine", "Kathleen", "Sandra", "Yael", "Frieda", "Emile", "Dane", "Carmella", "Rosalva", "Denita", "Marvis", "Vilma", "Lucila", "Coral", "James", "Jerald", "Buford", "Vennie"  
                   "Cathy", "Melody", "Siobhan", "Annmarie", "Tanna", "Liliana", "Keshia", "Irwin", "Jacqualine", "Leigh", "Sulema", "Marty", "Mike", "Shonta", "Lane", "Eldora", "Adah", "Leland", "Teresia", "Chloe", "Cordie", "Hal", "Sherryl", "Reggie", "Chery", "Columbus", "Edith"]
    
    pn = random.choice(name_random)
    ssn = random.randint(0, 9999999999)
    
    # ------------------------------------------------------------------------------------------------
    #  PATIENT ADMISSION
    # ------------------------------------------------------------------------------------------------

    #admission patient
    function_admission.preadmission_nonmed(
        todaynow,
        todaytime,
        str(pn),
        "Automated NM",
        str(pn),
        "02/07/1997",
        "Male",
        "Single",
        "American", 
        "english",
        ssn,
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
    
    #This function is to get the current browser url to get the link of the current patient dashboard
    #getlastpatient = config.driver.get(config.driver.current_url)
    getlastpatient = config.driver.current_url
    
    #oasis.getpatientlink(getlastpatient)
    
    time.sleep(5)
     
    
    
    
