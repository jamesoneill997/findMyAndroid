def enter_email(driver, email):
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div').click()

def enter_password(driver, password):
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()