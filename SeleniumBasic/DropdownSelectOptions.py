import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

#Static dropdown
selectLocator = driver.find_element(By.CSS_SELECTOR, '#dropdown-class-example')
select = Select(selectLocator)
select.select_by_visible_text('Option2')
#select.select_by_index(1)
assert selectLocator.get_attribute('value') == 'option2'

#dynamic dropdown
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
fromCity = driver.find_element(By.NAME, 'ctl00_mainContent_ddl_originStation1_CTXT')
fromCity.send_keys('ko')
time.sleep(2)
cities = driver.find_elements(By.XPATH, "//div[@class='dropdownDiv']/ul/li/a")
for city in cities:
   if city.text == 'Kolkata (CCU)':
       city.click()
       assert fromCity.get_attribute('value') == 'Kolkata (CCU)'




time.sleep(2)
driver.quit()
