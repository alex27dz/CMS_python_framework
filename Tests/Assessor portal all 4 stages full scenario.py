import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Timers
delay = 1
short_delay = 0.005
medium_delay = 2
long_delay = 12
start_time = time.perf_counter()

# User
user = ''

# Webdriver
webdriver_path = "C:/ADocuments/Python_framework/CMS_Python_framework/chromedriver"
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service)


print('Assessor portal all 4 stages - full scenario')  # put under a function at the end
def openweb(portal_link):
    driver.get(portal_link)  # Open Google website
    driver.maximize_window()
    time.sleep(short_delay)
    return True
def logging(user, password):
    logging = driver.find_element(By.XPATH, '//*[@id="main-content"]/app-safety-and-prevention-homepage/div/app-login-header/div/div/div[2]/app-login-register/div/div/div[2]/div/div[2]/div/button')
    logging.click()
    time.sleep(delay)
    email = driver.find_element(By.XPATH, '//*[@id="okta-signin-username"]')
    email.click()
    email.send_keys(user)
    passw = driver.find_element(By.XPATH, '//*[@id="okta-signin-password"]')
    passw.click()
    passw.send_keys(password)
    sign_in = driver.find_element(By.XPATH, '//*[@id="okta-signin-submit"]')
    sign_in.click()
    time.sleep(delay)
    return True

openweb('https://intra.stage.apps.labour.gov.on.ca/internal-portal-qa/#/program-delivery-applications')
logging()

