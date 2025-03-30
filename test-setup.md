Selenium is a tool which is widely used for testing, it has proper docs, multiple resources and large community. I have used Selenium in this assessment because it is easy to find an answer when you're stuck as it has a lot of resources online, and I have similar experience so it was easy for me to get started. Selenium supports cross browser compatibility (i have used only chrome here), as well as headless tests.

To get started,

1. Head over to https://github.com/krishchvn/linq-assessment, clone the repository using git clone https://github.com/krishchvn/linq-assessment.git
2. Make sure you have chrome stable version installed and check version using chrome://version in chrome url input (should be 132 or greater for smooth operations). Also, you should have python installed (preferably v3.10)
3. Install chromedriver of same major version as chrome (I'm using chromedriver v134 as I'm using chrome version 134.0.1)
4. Place chromedriver.exe in same directory as where you cloned the git repo.
5. You can install selenium and webdriver-manager using pip install selenium; pip install webdriver-manager or you can run requirements.text by pip install requirements.txt
6. Run command python run_all_tests.py.
