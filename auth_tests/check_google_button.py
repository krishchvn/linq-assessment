from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Google_Button_Test:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-insecure-localhost")
        chrome_options.add_argument('--disable-gpu')  
        chrome_options.add_argument('--disable-dev-shm-usage')  
        chrome_options.add_argument('--no-sandbox')  
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--disable-webrtc')
        chrome_options.add_argument("--log-level=3")  
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)

    def open_page(self, url):
        self.driver.get(url)
        time.sleep(1)
    
    def extract_shadow_root(self):
        try:
            shadow_host_level_0 = self.driver.find_element(By.CSS_SELECTOR, '#main')
            time.sleep(1)
            shadow_host_level_1 = self.driver.execute_script('return document.querySelector("#main > div > ion-content")', shadow_host_level_0)
            time.sleep(1)
            return shadow_host_level_1
        except:
            print("Error extracting shadow root")
            return None
    
    def click_google_btn(self, shadow_host_level_1):
        google_btn = shadow_host_level_1.find_element(By.CSS_SELECTOR, '#main > div > ion-content > div > div.rounded-l-2xl.flex-1.flex.flex-col.items-center.justify-center.glassmorphic.relative.px-6.py-8.flex.flex-col.items-center > div > div.flex.flex-col.gap-4.pb-4 > ion-button:nth-child(3)')
        google_btn.click()
        self.driver.implicitly_wait(2)
        original_window = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        google_btn_url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(original_window)
        return google_btn_url

    def quit(self):
        time.sleep(1)
        self.driver.quit()


