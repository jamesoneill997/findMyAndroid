#standard selenium libs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#To handle waiting
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#custom functions
from login import enter_email, enter_password
from ring import ring
import time
import os

#setup driver and timeout variables
driver = webdriver.chrome.webdriver.WebDriver(executable_path='./chromedriver')
timeout = 5

try:
    email = os.environ['pyemail']
    password = os.environ['pypassword']

except KeyError:
    print("You have not set up your credentials as environment variables. Please enter them now.")
    email = os.environ['pyemail'] = str(input("Please enter your Google email address: "))
    password = os.environ['pypassword'] = str(input("Please enter your Google password: "))

#open webpage
driver.get("https://www.google.com/android/find")

#credentials
enter_email(driver, email)
WebDriverWait(driver, timeout).until( EC.presence_of_element_located((By.ID, "passwordNext")))
enter_password(driver, password)
WebDriverWait(driver, timeout).until( EC.presence_of_element_located((By.ID, "device-infos")))

try:
    ring(driver)

except NoSuchElementException:
    time.sleep(2)
    ring(driver)