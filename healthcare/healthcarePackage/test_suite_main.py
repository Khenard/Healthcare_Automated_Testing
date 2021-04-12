import config
import login2

#Open Chrome and navigate to realtime workflow
config.driver.maximize_window()
config.driver.get("https://qado.medisource.com/login")

login2.login("superagent@unitest", "Tester2021!")




