from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys

class MainTest():
    
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver =webdriver.Chrome(options=options)
    
    def main_method(self):
        self.driver.get("https://www.saucedemo.com/")
        
        usernames = [elem.text for elem in self.driver.find_element(by="id", value="CustomerEmail").send_keys("") ]
        password = self.driver.find_element(by="id", value="CustomerPassword").send_keys("" + Keys.RETURN)

        self.driver.find_element(By.ID, 'user-name').send_keys("standard_user"[0])  # Using the first username
        self.driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        self.driver.find_element(By.ID, 'login-button').click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        login_header = self.driver.title

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
        titles = [elem.text for elem in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")[:5]]

        data = {
            "usernames": usernames,
            "password": password,
            "login_header": login_header,
            "product_titles": titles
        }

        self.driver.quit()
        return data

test = MainTest()
data = test.main_method()

