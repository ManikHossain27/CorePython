import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.maximize_window()
#navigate to url
url = 'https://rahulshettyacademy.com/AutomationPractice/'
try:
    driver.get(url)
except Exception as e:
    print(e)

#Check the Current url match with expected url and page title
assert driver.current_url == url
assert driver.title == 'Practice Page'

#Check box
checkBoxs = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkBox in checkBoxs:
   if checkBox.get_attribute('value') == 'option2':
       checkBox.click()
       assert checkBox.is_selected()
   else:
       assert not checkBox.is_selected()
#Button
radioButton = driver.find_elements(By.CLASS_NAME, 'radioButton')
radioButton[2].click()  #starts from 0
assert  radioButton[2].is_selected()


time.sleep(3)
driver.quit()
