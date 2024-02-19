#exercise 02
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service
import time


def get_web():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    info_data = webdriver.Chrome(options=options)
    info_data.get("https://titan22.com/account/login?return_url=%2Faccount")
    return info_data

def info_main():
    info_data = get_web()
    info_data.find_element(by="id", value="CustomerEmail").send_keys("") # Put of username
    time.sleep(2)
    info_data.find_element(by="id", value="CustomerPassword").send_keys("" + Keys.RETURN) # Put of password
    time.sleep(2)
    info_data.find_element(by="", value="").click()
    print(info_data.current_url)
    
print(info_main())
