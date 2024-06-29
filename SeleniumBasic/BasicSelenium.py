
from selenium import webdriver
from selenium.webdriver.common.by import By

#Connect Chrome driver
#driver = webdriver.Chrome()
#To ignore privacy problem
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

#maximize your browser
driver.maximize_window()
#go to this url
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
#Get title of this page
title = driver.title
#get current url of this page
currentUrl = driver.current_url
#print title
print('Title of the page:', title)
#print current url
print('Url of the current page:', currentUrl)
#implicit wait
driver.implicitly_wait(1)

#Enter name
driver.find_element(By.NAME, "name").send_keys("Manik Hossain")
#Enter Email
driver.find_element(By.NAME, 'email').send_keys('kinam@gmail.com')
#Select gender
radio1 = driver.find_element(By.XPATH, "//input[@id='gender']")
radio1.click()
if radio1.is_selected():
    print("Button is selected")
else:
    print("Button is not selected")
#Enter mobile no.
driver.find_element(By.CSS_SELECTOR, "input[id='mobile']").send_keys(12345678910)

#Select date of birth
driver.find_element(By.ID, 'dob').click()

# Wait for the calendar to appear (use WebDriverWait if needed)
driver.implicitly_wait(1)
# Locate and click the day corresponding to 14th
#driver.find_element(By.className("ui-datepicker-current-day")).click()


driver.quit()