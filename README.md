## linq-assessment

Hello!

## Prerequisites

Python 3.10 installed; Google Chrome >= v132 installed;

## Setup

1. Head over to https://github.com/krishchvn/linq-assessment, clone the repository using git clone https://github.com/krishchvn/linq-assessment.git
2. Make sure you have chrome stable version installed and check version using chrome://version in chrome url input (should be 132 or greater for smooth operations). Also, you should have python installed (preferably v3.10)
3. Install chromedriver of same major version as chrome (I'm using chromedriver v134 as I'm using chrome version 134.0.6998)
4. Place chromedriver.exe in same directory as where you cloned the git repo.
5. You can install selenium and webdriver-manager using pip install selenium; pip install webdriver-manager or you can run requirements.text by pip install requirements.txt
6. Run command python run_all_tests.py.

Warning: These tests are run on Windows, if you use MacOS or any Linux distro, be sure to update executable path for chromedriver

Code where change might be needed: `self.service = Service(executable_path="chromedriver.exe")`

## Test Structure

1.check_text.py - Checks visual text if visible on linqapp.com/welcome <br> 2.check_homepage_button.py - Checks homepage button functionality, to redirect to appropriate link<br> 3.auth_tests/ - folder containing tests to check authentication links<br> 4.auth_tests/check_email_button.py - checks if email auth button redirects to linqapp.com/auth-page and back button functionality<br> 5.auth_tests/check_apple_button.py - checks if apple auth button redirects to appropriate link <br>6.auth_tests/check_google_button.py - checks if google auth button redirects to appropriate link <br>7.auth_tests/check_linkedin_button.py - checks if linkedin auth button redirects to appropriate link

## Run Tests

Run command python run_all_tests.py and it should run all test files.

I've also added Github Actions and a potential bug in bug_report.md

Thank you for visiting!
