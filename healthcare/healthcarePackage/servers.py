import config, time, login

# ------------------------------------------------------------------------------------------------
#  QA SERVER
# ------------------------------------------------------------------------------------------------
def qaserver():
    config.driver.maximize_window()
    config.driver.get("https://qado.medisource.com/login")
    login.login("superagent@unitest", "Tester2021@")
    time.sleep(5)
# ------------------------------------------------------------------------------------------------
#  LIVE SERVER
# ------------------------------------------------------------------------------------------------
def liveserver():
    config.driver.maximize_window()
    config.driver.get("https://app.medisource.com/login")
    login.login("superagent@geekers", "Tester2021!")
    time.sleep(5)
    
