import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\\Users\\ndasa\\Downloads\\chromedriver_win32\\chromedriver.exe')

def get_drver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_drver()
    driver.find_element(by="id", value="id_username").send_keys("nxxxx@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("Nicoxxxx" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    print(driver.current_url)

print(main())
