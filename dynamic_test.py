from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('http://app.cloudqa.io/home/AutomationPracticeForm')

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="firstname"]')))

first_name_field = driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
first_name_field.send_keys('John')

last_name_field = driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
last_name_field.send_keys('Doe')

email_field = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
email_field.send_keys('john.doe@example.com')

submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_button.click()

wait.until(EC.url_contains('/confirmation'))

confirmation_message = driver.find_element(By.CSS_SELECTOR, '#confirmation-message').text
if 'Form Submitted Successfully' in confirmation_message:
    print('Form submitted successfully.')
else:
    print('Form submission failed.')

driver.quit()