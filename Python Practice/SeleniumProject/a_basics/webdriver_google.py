import time

from selenium import webdriver

driver = webdriver.Chrome("../recources/chromedriver.exe")
url = "https://www.google.com/"
driver.get(url)
assert driver.title == "Google", "Page does not match"
print(driver.title)
element = driver.find_element(by="name", value="q")
element.send_keys("selenium")
driver.find_element(by="name", value="btnK").submit()
time.sleep(3)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
driver.maximize_window()
time.sleep(2)
driver.minimize_window()

driver.close()