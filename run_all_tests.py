from check_text import Visual_Text_Test
from check_homepage_button import HomePage_Button_Test
from auth_tests.check_apple_button import Apple_Button_Test
from auth_tests.check_email_button import Email_Button_Test
from auth_tests.check_google_button import Google_Button_Test
from auth_tests.check_linkedin_button import Linkedin_Button_Test

if __name__ == "__main__":
    url = "https://linqapp.com/welcome"

    test = Visual_Text_Test()
    test.open_page(url)
    text = test.extract_shadow_roots_and_text()
    
    if text == "One Platform to Meet, Manage, and Close.":
        print("✅ Visual Test Case Passed")
    else:
        print("❌ Visual Test Case Failed")
    
    test.quit()

    test = HomePage_Button_Test()
    test.open_page(url)
    homepage_url = test.extract_shadow_roots_and_button()
    if homepage_url == "https://linqapp.com/":
        print("✅ HomePage Button -> Homepage Test Case Passed")
    else:
        print("❌ HomePage Button -> Homepage Test Case Failed")
    
    test.quit()

    test = Apple_Button_Test()
    test.open_page(url)
    shadow_host_level_1 = test.extract_shadow_root()
    if shadow_host_level_1:
        apple_url = test.click_apple_btn(shadow_host_level_1)
        if "https://appleid.apple.com/auth/authorize" in apple_url:
            print("✅ Apple Auth Button Test Case Passed")
    else:
        print("❌ Apple Auth Button Test Case Failed")
    
    test.quit()

    test = Email_Button_Test()
    test.open_page(url)
    shadow_host_level_1 = test.extract_shadow_root()
    if shadow_host_level_1:
        test.click_email_btn(shadow_host_level_1)
        shadow_host_level_1_copy = test.extract_shadow_root()
        staging_url = test.return_to_staging_page(shadow_host_level_1_copy)
        if staging_url == url:
            print("✅ Email Auth Button Test Case Passed")
    else:
        print("❌ Email Auth Button Test Case Failed")
    
    test.quit()

    test = Google_Button_Test()
    test.open_page(url)
    shadow_host_level_1 = test.extract_shadow_root()
    if shadow_host_level_1:
        google_btn_url = test.click_google_btn(shadow_host_level_1)
        if "https://accounts.google.com/v3/signin" in google_btn_url:
            print("✅ Google Auth Button Test Case Passed")
    else:
        print("❌ Google Auth Button Test Case Failed")
    
    test.quit()

    test = Linkedin_Button_Test()
    test.open_page(url)
    shadow_host_level_1 = test.extract_shadow_root()
    if shadow_host_level_1:
        linkedin_btn_url = test.click_linkedin_btn(shadow_host_level_1)
        if "https://www.linkedin.com/uas/login" in linkedin_btn_url:
            print("✅ Linkedin Auth Button Test Case Passed")
    else:
        print("❌ Linkedin Auth Button Test Case Failed")
    
    test.quit()