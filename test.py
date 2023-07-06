from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the web page
driver.get('http://app.cloudqa.io/home/AutomationPracticeForm')

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'first-name')))

# Test the first field
first_name_field = driver.find_element(By.ID, 'first-name')
first_name_field.send_keys('John')

# Test the second field
last_name_field = driver.find_element(By.ID, 'last-name')
last_name_field.send_keys('Doe')

# Test the third field
email_field = driver.find_element(By.ID, 'email')
email_field.send_keys('john.doe@example.com')

# Submit the form
submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

# Wait for the form submission to complete
wait.until(EC.url_contains('/confirmation'))

# Verify the submission was successful
confirmation_message = driver.find_element(By.ID, 'confirmation-message').text
if 'Form Submitted Successfully' in confirmation_message:
    print('Form submitted successfully.')
else:
    print('Form submission failed.')

# Close the browser
driver.quit()
