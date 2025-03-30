from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage_Button_Test:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-insecure-localhost")
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)

    def open_page(self, url):
        self.driver.get(url)
        time.sleep(1)
    
    def extract_shadow_roots_and_button(self):
        try:
            shadow_host_level_0 = self.driver.find_element(By.CSS_SELECTOR, '#main')
            time.sleep(1)
            shadow_host_level_1 = self.driver.execute_script('return document.querySelector("#main > div > ion-content")', shadow_host_level_0)
            time.sleep(1)
            svg_btn = shadow_host_level_1.find_element(By.CSS_SELECTOR, '#main > div > ion-content > div > div.flex-1.flex.flex-col-reverse.py-8.justify-between.relative.text-white.px-4.px-8 > button > svg')
            svg_btn.click()
            time.sleep(2)
            return self.driver.current_url
        except:
            print("Error extracting shadow root")
            return None
    
    def quit(self):
        time.sleep(1)
        self.driver.quit()
        

