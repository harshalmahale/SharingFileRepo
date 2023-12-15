from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://www.opencart.com/index.php?route=account/register"
driver.get(url)
driver.maximize_window()

dropcountry = Select(driver.find_element(By.XPATH,"//*[@id='input-country']"))

#Select option from dropdown

# dropcountry.select_by_visible_text("India")
# dropcountry.select_by_value("30")
# dropcountry.select_by_index(13)

# Capture all the options and print them

dropdownoptions = dropcountry.options
print("All the options are: ",len(dropdownoptions))

for opt in dropdownoptions:
    print(opt.text)

for opt in dropdownoptions:
    if opt.text == "India":
        opt.click()
        break


driver.close()