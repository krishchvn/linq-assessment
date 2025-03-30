from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Visual_Text_Test:
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
    
    def extract_shadow_roots_and_text(self):
        try:
            shadow_host_level_0 = self.driver.find_element(By.CSS_SELECTOR, '#main')
            time.sleep(1)
            shadow_host_level_1 = self.driver.execute_script('return document.querySelector("#main > div > ion-content")', shadow_host_level_0)
            time.sleep(1)
            text_1 = shadow_host_level_1.find_element(By.CSS_SELECTOR, '#main > div > ion-content > div > div.flex-1.flex.flex-col-reverse.py-8.justify-between.relative.text-white.px-4.px-8 > div.flex.flex-col.gap-6.text-\[38px\].font-outfit-600.leading-10 > div.text-\[38px\].font-outfit-300').text
            text_2 = shadow_host_level_1.find_element(By.CSS_SELECTOR, '#main > div > ion-content > div > div.flex-1.flex.flex-col-reverse.py-8.justify-between.relative.text-white.px-4.px-8 > div.flex.flex-col.gap-6.text-\[38px\].font-outfit-600.leading-10 > div:nth-child(2)').text
            text_3 = shadow_host_level_1.find_element(By.CSS_SELECTOR, '#main > div > ion-content > div > div.flex-1.flex.flex-col-reverse.py-8.justify-between.relative.text-white.px-4.px-8 > div.flex.flex-col.gap-6.text-\[38px\].font-outfit-600.leading-10 > div:nth-child(3)').text
            return text_1 + " " + text_2 + " " + text_3
        except:
            print("Error extracting shadow root")
            return None
    
    def quit(self):
        time.sleep(1)
        self.driver.quit()
        

# if __name__ == "__main__":
#     url = "https://linqapp.com/welcome"

#     test = Visual_Text_Test()
#     test.open_page(url)
#     text = test.extract_shadow_roots_and_text()
#     if text == "One Platform to Meet, Manage, and Close.":
#         print("✅ Visual Test Case Passed")
#     else:
#         print("❌ Visual Test Case Failed")
    
#     test.quit()