import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.maximize_window()
#navigate to url
url = 'https://demo.automationtesting.in/Alerts.html'
try:
    driver.get(url)
except Exception as e:
    print(e)

#Check the Current url match with expected url and page title
assert driver.current_url == url
print(driver.title)
#assert driver.title == 'Practice Page'

#Alert
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-danger']").click()
try:
    alert = driver.switch_to.alert
    alertText = alert.text
    print(alertText)
    alert.accept()
except:
    print("no alert")

#Alert 2
driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
try:
    alert = driver.switch_to.alert
    alertText = alert.text
    print(alertText)
    alert.dismiss()
except:
    print("no alert")

#Alert 3
driver.find_element(By.XPATH, "//a[text()='Alert with Textbox ']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-info']").click()
try:
    alert = driver.switch_to.alert
    alertText = alert.text
    print(alertText)
    alert.send_keys('Kinam')
    alert.accept()
except:
    print("no alert")

condMessage = driver.find_element(By.ID, "demo1").text
assert 'Kinam' in condMessage



driver.quit()