import config, time
from selenium.webdriver.common.keys import Keys

def admission(
        refdate,
        reftime,
        plannedsoc,
        lname,
        fname,
        mi,
        sfx,
        bdate,
        mstatus,
        ethn,
        langspoken,
        ssnumber,
        streetaddress,
        adddirection,
        majorcstreet,
        city,
        stateadd,
        zipcodeadd
        ):
    #Navigate to Add patient page
    config.driver.get("https://qado.medisource.com/patient")
    time.sleep(5)
    
    #get element and assign variables
    skip_eligibility = config.driver.find_element_by_link_text("Skip").click() #skip button
    
    
    
    #Patient Information
    referral_date = config.driver.find_element_by_id("refDate").send_keys(refdate)
    referral_time = config.driver.find_element_by_id("referral_time").send_keys(reftime)
    mrn = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/label/input").click()
    preadmission_date = config.driver.find_element_by_id("pre_admission_date").send_keys(plannedsoc)
    last_name = config.driver.find_element_by_id("last_name").send_keys(lname)
    first_name = config.driver.find_element_by_id("first_name").send_keys(fname)
    middle_initial = config.driver.find_element_by_id("mi").send_keys(mi)
    suffix = config.driver.find_element_by_id("suffix").send_keys(sfx)
    birthdate = config.driver.find_element_by_id("birthdate").send_keys(bdate)
    gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[1]/input").click() #male
    #code for choosing select
    option = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/a").click() #click the select
    mstext = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/div/div/input").send_keys(mstatus, Keys.ENTER) #search the value
    option = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").click()
    ethnicity = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").send_keys(ethn, Keys.ENTER)
    option = config.driver.find_element_by_xpath("//*[@id='language_spoken']/div[1]/input").click()
    languagespoken = config.driver.find_element_by_xpath("//*[@id='language_spoken']/div[1]/input").send_keys(langspoken, Keys.ENTER)
    ssn = config.driver.find_element_by_id("ssNumber").send_keys(ssnumber)
    #Patient Address
    strtadd = config.driver.find_element_by_id("main_line1").send_keys(streetaddress)
    addd = config.driver.find_element_by_id("main_line2").send_keys(adddirection)
    mcs = config.driver.find_element_by_id("main_street").send_keys(majorcstreet)
    cityadd = config.driver.find_element_by_id("main_city").send_keys(city)
    
    option = config.driver.find_element_by_css_selector("main_state").click() #click the select
    time.sleep(5)
    state = config.driver.find_element_by_xpath("//*[@id='main_state_chosen']/div/div/input").send_keys(stateadd, Keys.ENTER) #search the value
    time.sleep(5)
    
    zipcode = config.driver.find_element_by_id("main_zipcode").send_keys(zipcodeadd)
    
    




    time.sleep(5)
