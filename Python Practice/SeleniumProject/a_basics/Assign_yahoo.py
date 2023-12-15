from selenium import webdriver
import time
driver = webdriver.Chrome("../recources/chromedriver.exe")
url = "https://login.yahoo.com/"
driver.get(url)
# time.sleep(2)
driver.maximize_window()
driver.find_element(by="id", value="login-username").send_keys("harshal_mahale@yahoo.com")
driver.implicitly_wait(5)
driver.find_element(by="name", value="signin").click()
# time.sleep(2)
driver.find_element(by="id", value="login-passwd").send_keys("Persistent@1999")
# time.sleep(2)
driver.find_element(by="id", value="login-signin").click()
time.sleep(2)
driver.close()


