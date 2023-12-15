from selenium import webdriver
import time
driver = webdriver.Chrome("../recources/chromedriver.exe")
# driver.implicitly_wait(5)
# url = "https://www.google.com/"
# driver.get(url)
# assert driver.title == "Google", "Page does not match"
# print(driver.title)
# element = driver.find_element(by="name", value="q")
# element.send_keys("selenium")
# driver.find_element(by="name", value="btnK").submit()

url = "http://cookbook.seleniumacademy.com/Config.html"
driver.get(url)     # visit the url
print(driver.title)
time.sleep(2)
driver.find_elements(by="name", value="fuel_type")[1].click()
time.sleep(2)
element_airbags = driver.find_element(by="name", value="airbags")
if not element_airbags.is_selected():
    driver.find_element(by="name", value="airbags").click()
time.sleep(5)

driver.close()