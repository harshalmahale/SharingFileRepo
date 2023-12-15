from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
chromeServicePath = Service("../recources/chromedriver.exe")
driver = webdriver.Chrome(service=chromeServicePath)
url = "http://www.cookbook.seleniumacademy.com/Alerts.html"
driver.get(url)
# create action chain object
driver.implicitly_wait(5)
action = ActionChains(driver)

driver.find_element(By.XPATH,"//*[@id='simple']").click()

alert = driver.switch_to.alert
alert_message = alert.text
#alert.accept()
assert alert_message == "Hello! I am an alert box!"
# alert = driver.switch_to.alert
#   alert_message = alert.text
#   alert.accept()