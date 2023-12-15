from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self

# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Rolex Rings')]/self::a").text
# print(text_msg)

text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Rolex Rings')]/ancestor::tr").text
print(text_msg)

driver.close()

# parent
text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Rolex Rings')]/parent::td").text
print(text_msg)

#child

childs = driver.find_elements(By.XPATH,"//a[contains(text(),'Rolex Rings')]/ancestor::tr/child::td")
print(len(childs))