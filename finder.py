from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.chrome.webdriver.WebDriver(executable_path='../../../chromedriver')

driver.get("https://www.facebook.com/")