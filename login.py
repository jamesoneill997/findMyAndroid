def enter_email(driver, email):
    driver.find_element_by_id('Email').send_keys(email)
    driver.find_element_by_id('next').click()
    

def enter_password(driver, password):
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('submit').click()
