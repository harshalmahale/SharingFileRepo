from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

url = "https://itera-qa.azurewebsites.net/home/automation"
driver.get(url)

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
#----------For selecting all checkboxes--------
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# for checkbox in checkboxes:
#     checkbox.click()

#--------For selecting last two checkboxes--------
time.sleep(5)
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(2)

#-----For selecting multiple checkboxes by choices

for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname=='monday' or weekname=='sunday':
        checkbox.click()

time.sleep(2)
driver.close()