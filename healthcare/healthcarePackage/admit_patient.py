import config, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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
        zipcodeadd,
        phoneone,
        phonetwo,
        emaila,
        cgname, 
        cgphone,
        ecname,
        ecrel,
        ecp1,
        ecp2
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
    
    #Language Spoken
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").click()
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(langspoken)
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(Keys.ENTER)

    ssn = config.driver.find_element_by_id("ssNumber").send_keys(ssnumber)
    
    #Patient Address
    strtadd = config.driver.find_element_by_id("main_line1").send_keys(streetaddress)
    addd = config.driver.find_element_by_id("main_line2").send_keys(adddirection)
    mcs = config.driver.find_element_by_id("main_street").send_keys(majorcstreet)
    cityadd = config.driver.find_element_by_id("main_city").send_keys(city)
    
    #State Code
    config.driver.find_element(By.XPATH, "//tr[20]/td[2]/div/div/div/a").click()
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").click()
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").send_keys(stateadd, Keys.ENTER)

    zipcode = config.driver.find_element_by_id("main_zipcode").send_keys(zipcodeadd)
    phone1 = config.driver.find_element_by_name("phone").send_keys(phoneone)
    phone2 = config.driver.find_element_by_name("other_phone").send_keys(phonetwo)
    email = config.driver.find_element_by_name("main_email").send_keys(emaila)
    
    #same as patient address button
    sameaspatientaddress = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[25]/td[2]/button").click()

    #Living Situation
    livings = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[35]/td[2]/div/label[2]/input").click() #Lives Alone
    assistance = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[36]/td[2]/div/label[4]/input").click() #Occasional short-term
    ls_caregiver = config.driver.find_element_by_id("ls_caregiver").send_keys(cgname)
    ls_caregiver_phone = config.driver.find_element_by_id("ls_caregiver_phone").send_keys(cgphone)
    
    #Emergency Contact
    ec_name = config.driver.find_element_by_id("ec_name").send_keys(ecname)
    ec_relationship = config.driver.find_element_by_id("ec_relationship").send_keys(ecrel)
    ec_phone = config.driver.find_element_by_id("ec_phone").send_keys(ecp1)
    ec_other_phone = config.driver.find_element_by_id("ec_other_phone").send_keys(ecp2)
    
    #Physician Information
    config.driver.find_element(By.CSS_SELECTOR, "#physician_attending_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, ".active-result:nth-child(2)").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#physician_primary_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, "#physician_primary_chosen .active-result:nth-child(2)").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#primary_insurance_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, "#primary_insurance_chosen .active-result:nth-child(2)").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#secondary_insurance_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(51) .fg-line").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#admissiontype_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, ".active-result:nth-child(1)").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#point_of_origin_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, "#point_of_origin_chosen .active-result:nth-child(1)").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#referral_type_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, "#referral_type_chosen .active-result:nth-child(1)").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#referral_type_chosen span").click()
    config.driver.find_element(By.CSS_SELECTOR, "#referral_type_chosen .active-result:nth-child(2)").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#referral_source_id_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, "#referral_source_id_chosen .active-result:nth-child(2)").click()
    
    config.driver.find_element(By.CSS_SELECTOR, "#hospital_id_chosen > .chosen-single").click()
    config.driver.find_element(By.CSS_SELECTOR, "#hospital_id_chosen .active-result").click()
    
    
    
    
    
    
    time.sleep(5)
