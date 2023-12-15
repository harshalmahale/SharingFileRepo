from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

url = "https://www.nopcommerce.com/en/demo"
driver.get(url)

#Find the number of links in the page

# links = driver.find_elements(By.TAG_NAME,'a')
links = driver.find_elements(By.XPATH,'//a')
print("Total numbers of links",len(links))

# driver.close()

# Print all links

for link in links:
    print(link.text)
driver.close()
