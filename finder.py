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


timeout = 5


driver = webdriver.chrome.webdriver.WebDriver(executable_path='./chromedriver')


driver.get("https://www.google.com/android/find")

enter_email(driver, email)

WebDriverWait(driver, timeout).until( EC.presence_of_element_located((By.ID, "passwordNext")))

try:
    enter_password(driver, password)

except ElementNotInteractableException:
    time.sleep(2)
    enter_password(driver, email)

WebDriverWait(driver, timeout).until( EC.presence_of_element_located((By.ID, "device-infos")))

try:
    ring(driver)

except NoSuchElementException:
    time.sleep(2)
    ring(driver)