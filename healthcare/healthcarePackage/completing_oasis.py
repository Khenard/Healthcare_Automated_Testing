import config, time, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from _ast import Div

ssn = random.randint(0, 9999999999)
# ------------- Time In and Time Out -----------------------------------------------------------------------------------
def oasissoc_timeinout(ti, to):
    timein = config.driver.find_element_by_name("timeIn").send_keys(ti)
    timeout = config.driver.find_element_by_name("timeOut").send_keys(to)

# ------------- Demographics -----------------------------------------------------------------------------------
def oasissoc_demographics(todaynow, episodetiming):
    m0063 = config.driver.find_element_by_id("M0063_MEDICARE_NUM").send_keys(ssn)
    m0090 = config.driver.find_element_by_id("m0090_info_completed_dt").send_keys(todaynow)
    time.sleep(3)
    m0102_checkbox = config.driver.find_element_by_name("M0102_PHYSN_ORDRD_SOCROC_DT_NA").click()
    time.sleep(3)
    m0104 = config.driver.find_element_by_id("m0104_physn_rfrl_dt").send_keys(todaynow)
    
    #For Episode Timing
    etiming = ""
    if episodetiming == "Early":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[1]/div[1]/label/input")
    elif episodetiming == "Later":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[1]/div[2]/label/input")
    elif episodetiming == "Unknown":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[2]/div[1]/label/input")
    elif episodetiming == "NA":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[2]/div[2]/label/input")
    etiming.click()
    
    m0140_asian = config.driver.find_element_by_xpath("//*[@id='M0140_ETHNIC_ASIAN']/input").click()
    m0150_medicare_trad = config.driver.find_element_by_xpath("//*[@id='M0150_CPAY_MCARE_FFS']/input").click()
    #m0150_private_insurance = config.driver.find_element_by_xpath("//*[@id='M0150_CPAY_PRIV_INS']/input").click()
    m1000_skilled_nursing_facility = config.driver.find_element_by_name("M1000_DC_SNF_14_DA").click()
    m1005_unknown = config.driver.find_element_by_name("M1005_INP_DSCHG_UNKNOWN").click()
    
# ------------- Diagnosis ----------------------------------------------------------------------------------- 
def oasissoc_diagnosesmedhis(
        pdx,
        sdx1,
        sdx2,
        sdx3,
        sdx4,
        sdx5,
        m1028_items,
        m0133_items,
        mheight,
        mweight
        ):
    time.sleep(5)
    
    #Primary Diagnosis
    pd = config.driver.find_element_by_xpath("//*[@id='tooltip_a']/table/tbody/tr/td[2]/icd-opt/div/div[1]/input")
    pd.send_keys(pdx)
    time.sleep(1)
    config.driver.switch_to_active_element()
    pd.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    pd.send_keys(Keys.ENTER)
    pdr = config.driver.find_element_by_xpath("//*[@id='icdSeverityIdCode$index']/label[4]/input").click()
    
    #Secondary Diagnosis
    #1st Secondary Diagnosis
    sd1 = config.driver.find_element_by_xpath("//*[@id='tooltip_b']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd1.send_keys(sdx1)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd1.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    sd1.send_keys(Keys.ENTER)
    sd1r = config.driver.find_element_by_xpath("//*[@id='tooltip_b']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3
    
    #2nd Secondary Diagnosis
    sd2 = config.driver.find_element_by_xpath("//*[@id='tooltip_c']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd2.send_keys(sdx2)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd2.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    sd2.send_keys(Keys.ENTER)
    sd2r = config.driver.find_element_by_xpath("//*[@id='tooltip_c']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3

    #3rd Secondary Diagnosis
    sd3 = config.driver.find_element_by_xpath("//*[@id='tooltip_d']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd3.send_keys(sdx3)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd3.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    sd3.send_keys(Keys.ENTER)
    sd3r = config.driver.find_element_by_xpath("//*[@id='tooltip_d']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3

    #4th Secondary Diagnosis
    sd4 = config.driver.find_element_by_xpath("//*[@id='tooltip_e']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd4.send_keys(sdx4)
    time.sleep(1)
    config.driver.switch_to_active_element()
    sd4.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    sd4.send_keys(Keys.ENTER)
    sd4r = config.driver.find_element_by_xpath("//*[@id='tooltip_e']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3

    #5th Secondary Diagnosis
    sd5 = config.driver.find_element_by_xpath("//*[@id='tooltip_f']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd5.send_keys(sdx5)
    time.sleep(2)
    config.driver.switch_to_active_element()
    sd5.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    sd5.send_keys(Keys.ENTER)
    sd5r = config.driver.find_element_by_xpath("//*[@id='tooltip_f']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3

    #m0128_items
    m1028_items_selected = ""
    for x in m1028_items:
        print(x)
        m1028_items_selected = config.driver.find_element_by_xpath("//*[@class='m-0']/label["+str(x)+"]/input")
        m1028_items_selected.click()
    time.sleep(2)
    
    m1030 = config.driver.find_element_by_xpath("//*[@id='M1030_THH_NONE_ABOVE']/input").click() #Value is None of the above
    
    #m0133_items
    m0133_items_selected = ""
    for x in m0133_items:
        print(x)
        m0133_items_selected = config.driver.find_element_by_xpath("//*[@id='M1033_HOSP_RISK_HSTRY_FALLS']/label["+ str(x) +"]/input")
        m0133_items_selected.click()
    time.sleep(2)
    m1060_height = config.driver.find_element_by_name("M1060_HEIGHT_A").send_keys(mheight)
    m1060_weight = config.driver.find_element_by_name("M1060_WEIGHT_B").send_keys(mweight)
    time.sleep(2)
    
    #Past Medical History   Select all No History
    pmh_s_nh = config.driver.find_element_by_name("SOOMEDICAL0135").click()
    pmh_i_nh = config.driver.find_element_by_name("SOOMEDICAL0121").click()
    pmh_e_nh = config.driver.find_element_by_name("SOOMEDICAL0137").click()
    pmh_r_nh = config.driver.find_element_by_name("SOOMEDICAL0138").click()
    pmh_c_nh = config.driver.find_element_by_name("SOOMEDICAL0139").click()
    pmh_g_nh = config.driver.find_element_by_name("SOOMEDICAL0141").click()
    pmh_n_nh = config.driver.find_element_by_name("SOOMEDICAL0142").click()
    pmh_m_nh = config.driver.find_element_by_name("SOOMEDICAL0143").click()
    pmh_cl_nh = config.driver.find_element_by_name("SOOMEDICAL0145").click()
    pmh_oh_nh = config.driver.find_element_by_name("SOOMEDICAL0146").click()
    pmh_s_nh = config.driver.find_element_by_name("SOOMEDICAL0147").click()

# ------------- Vital Signs / Sensory -----------------------------------------------------------------------------------  
def oasissoc_vssensory(
        vstemp,
        vspulse,
        vsres,
        vslasys,
        vsladyl,
        vso2room,
        vso2o2,
        vso2lpm,
        vsbs
        ):
    time.sleep(5)
    
    vs_temp = config.driver.find_element_by_name("SOOVS0001").send_keys(vstemp)
    vs_temp_scan = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/div/label[2]/input").click() #scan
    
    vs_pulse = config.driver.find_element_by_name("SOOVS0003").send_keys(vspulse)
    vs_pulse_radial = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[3]/td/table/tbody/tr/td[3]/div/label[1]/input").click()
    vs_res = config.driver.find_element_by_name("SOOVS0006").send_keys(vsres)
    
    vs_lefta_sys = config.driver.find_element_by_name("SOOVS0009").send_keys(vslasys)
    vs_lefta_dyl = config.driver.find_element_by_name("SOOVS0059").send_keys(vsladyl)
    vs_lefta_sitting = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[5]/td/table/tbody/tr/td[3]/div/label[1]/input").click()
    
    vs_o2room = config.driver.find_element_by_name("SOOVS0021").send_keys(vso2room)
    vs_o2o2 = config.driver.find_element_by_name("SOOVS0022").send_keys(vso2o2)
    vs_o2lpm = config.driver.find_element_by_name("SOOVS0023").send_keys(vso2lpm)
    
    vs_bs = config.driver.find_element_by_name("SOOVS0024").send_keys(vsbs)
    vs_bs_rbs = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[11]/td/table/tbody/tr/td[3]/div/label[2]/input").click()
    
    vs_weight_actual = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[12]/td/table/tbody/tr/td[3]/div/label[2]/input").click()
    vs_height_actual = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[13]/td/table/tbody/tr/td[3]/div/label[1]/input").click()
    
    m1242_nopain = config.driver.find_element_by_xpath("//*[@id='M1242_PAIN_FREQ_ACTVTY_MVMT']/div/div[1]/label/input").click()
    m1200_normalvision = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/div/label/input").click()
    
    #All sensory status will be WNL
    ss_eyes_wnl = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/table[4]/tbody/tr[2]/td/table/tbody/tr/td[2]/label/input").click()
    ss_ear_wnl = config.driver.find_element_by_name("SOOSENSORY0039").click()
    ss_mouth_wnl = config.driver.find_element_by_name("SOOSENSORY0059").click() 
    ss_nose_wnl = config.driver.find_element_by_name("SOOSENSORY0055").click() 
    ss_throat_wnl = config.driver.find_element_by_name("SOOSENSORY0063").click() 
    ss_speech_wnl = config.driver.find_element_by_name("SOOSENSORY0067").click() 
    ss_touch_wnl = config.driver.find_element_by_name("SOOSENSORY0070").click() 
    
# ------------- Integumentary / Endocrine -----------------------------------------------------------------------------------
def oasissoc_integendo():
    time.sleep(5)
    is_wnl = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input").click()
    bsppsr_noimpairement = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_rarelymoist = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[3]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_walksf = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[4]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_nolimit = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[5]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_excellent = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[6]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_noprob = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[7]/td[1]/table/tbody/tr[4]/td[1]/label/input").click()
    
    m1306_0 = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/label[1]/input").click()
    m1322_0 = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[5]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div/div[1]/label/input").click()
    m1324_na = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[6]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div/div[5]/label/input").click()
    m1330_0 = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[7]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input").click()
    m1340_0 = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[10]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input").click()
    
    endosys_wnl = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[3]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input").click()

# ------------- Cardiopulmonary -----------------------------------------------------------------------------------
def oasissoc_cardio():
    time.sleep(5)
    m1400_0 = config.driver.find_element_by_xpath('//*[@id="M1400_WHEN_DYSPNEIC"]/div[1]/label/input').click()
    resps_wnl = config.driver.find_element_by_xpath('//*[@id="cardioForm"]/div/fieldset/div[1]/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    cardio_wnl = config.driver.find_element_by_xpath('//*[@id="cardioForm"]/div/fieldset/div[1]/table[10]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    
# ------------- Nutrition / Elimination -----------------------------------------------------------------------------------
def oasissoc_nutrielim():
    time.sleep(5)
    uppergistat_wnl = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    genitostat_wnl = config.driver.find_element_by_xpath('//*[@id="SOOELIMINATION0011"]/td/table/tbody/tr/td[2]/div/label/input').click()
    abnelim_no = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[10]/tbody/tr[5]/td[2]/label[1]/input').click()
    spx_no = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[10]/tbody/tr[7]/td[2]/label[1]/input').click()
    m1600_0 = config.driver.find_element_by_xpath('//*[@id="M1600_UTI"]/div[1]/label/input').click()
    m1610_0 = config.driver.find_element_by_xpath('//*[@id="M1610_UR_INCONT"]/div[1]/label/input').click()
    lowergistat_wnl = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[20]/tbody/tr[1]/td[2]/label[1]/input').click()
    m1620_na = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[22]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div/div[7]/label').click()
    m1630_0 = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[23]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div/label[1]/input').click()
    
# ------------- Neurologic / Behavioral -----------------------------------------------------------------------------------
def oasissoc_neurobehav():
    time.sleep(5)
    neurostat_wnl = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    m1700_0 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[2]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1710_0 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr[1]/td/div/label/input').click()
    m1720_0 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[4]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1730_0 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[5]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1740_7 = config.driver.find_element_by_id('M1740_BD_NONE').click()
    m1745_1 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[7]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[2]/label/input').click()
    thought_wnl = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[9]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    languageb_no = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[10]/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/label/input').click()
    learningb_no = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[10]/tbody/tr[4]/td[2]/table/tbody/tr/td/label/input').click()
    soabuse = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[10]/tbody/tr[6]/td[2]/table/tbody/tr/td/label/input').click()
    spiritual_no = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[10]/tbody/tr[8]/td[2]/table/tbody/tr/td/label/input').click()
    
# ------------- ADL / IADL / Musculoskeletal -----------------------------------------------------------------------------------
def oasissoc_adlmusco():
    time.sleep(5)
    musstat_wnl = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td/div[2]/label/input').click()
    m1800_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[6]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1810_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[7]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1820_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[8]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1830_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[9]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1840_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[10]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1845_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[11]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1850_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[12]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1860_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[13]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1870_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[14]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1910_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[15]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    
    time.sleep(2)
    gg0100_a = config.driver.find_element_by_xpath('//div[@id="GG0100A_chosen"]/a/div/b').send_keys(Keys.ENTER)
    time.sleep(2)
    gg0100_b = config.driver.find_element_by_xpath('//div[@id="GG0100B_chosen"]/a/div/b').send_keys(Keys.ENTER)
    time.sleep(2)
    gg0100_c = config.driver.find_element_by_xpath('//div[@id="GG0100C_chosen"]/a/div/b').send_keys(Keys.ENTER)

       
    #musstat_wnl = config.driver.find_element_by_xpath('').click()
    #musstat_wnl = config.driver.find_element_by_xpath('').click()



# ------------- Medication -----------------------------------------------------------------------------------

# ------------- Care Management -----------------------------------------------------------------------------------




    #config.driver.close()
    
    