from selenium import webdriver

# from selenium.webdriver.common.by import By

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver


driver = headless_chrome()

url = "https://timesofindia.indiatimes.com/?from=mdr"
driver.get(url)
driver.maximize_window()

print(driver.title)
print(driver.current_url)