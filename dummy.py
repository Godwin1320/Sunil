import pyautogui as pyautogui
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service

driver = webdriver.Firefox()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

time.sleep(5)
usernam = driver.find_element(By.NAME, "username").send_keys("Admin")
passw = driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--active").send_keys("admin123")
submit1 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Dashboard
##########  Time for work #############
element0 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "i[class='oxd-icon bi-stopwatch']"))
)
element0.click()
time.sleep(5)
driver.back()

############  My Actions ############
element01 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='(1) Candidate to Interview']"))
)
element01.click()
time.sleep(5)
driver.back()
element01 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='(1) Pending Self Review']"))
)
element01.click()
time.sleep(5)
driver.back()

##########  Quick Launch ###########
element1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Assign Leave'] svg"))
)
element1.click()
time.sleep(5)
driver.back()
element2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Leave List'] svg"))
)
element2.click()
time.sleep(5)
driver.back()
element3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Timesheets'] svg"))
)
element3.click()
time.sleep(5)
driver.back()
element4 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Apply Leave'] svg"))
)
element4.click()
time.sleep(5)
driver.back()
element5 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='My Leave'] svg"))
)
element5.click()
time.sleep(5)
driver.back()
element6 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='My Timesheet'] svg"))
)
element6.click()
time.sleep(5)
driver.back()

###########  Buzz ############
element7 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-buzz-widget-header"))
)
element7.click()
time.sleep(5)
driver.back()

############# Employees on Leave Today  ###########
element8 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-icon.bi-gear-fill.orangehrm-leave-card-icon"))
)
element8.click()
time.sleep(5)
enable = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-switch-input.oxd-switch-input--active.--label-right"))
)
enable.click()
time.sleep(5)
submit = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
)
submit.click()
time.sleep(5)
element8.click()
time.sleep(5)
cancel_button = driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
time.sleep(5)
element8.click()
time.sleep(5)
close_button = driver.find_element(By.CSS_SELECTOR, ".oxd-dialog-close-button.oxd-dialog-close-button-position").click()

#############   pie cart number 1 ###########
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='Engineering']"))
    )
    element.click()
    time.sleep(5)
    element.click()
except TimeoutException:
    print(f"Element with CSS selector not found. Skipping to the next.")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='Human Resources']"))
    )
    element.click()
    time.sleep(5)
    element.click()
except TimeoutException:
    print(f"Element with CSS selector not found. Skipping to the next.")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='Administration']"))
    )
    element.click()
    time.sleep(5)
    element.click()
except TimeoutException:
    print(f"Element with CSS selector not found. Skipping to the next.")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='Client Services']"))
    )
    element.click()
    time.sleep(5)
    element.click()
except TimeoutException:
    print(f"Element with CSS selector not found. Skipping to the next.")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@title='Unassigned'][normalize-space()='Unassigned'])[1]"))
    )
    element.click()
    time.sleep(5)
    element.click()
except TimeoutException:
    print(f"Element with CSS selector not found. Skipping to the next.")

############  pie chart 2 #######################
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='Texas R&D']"))
    )
    element.click()
    time.sleep(5)
    element.click()
except TimeoutException:
    print(f"Element with CSS selector not found. Skipping to the next.")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='New York Sales Office']"))
    )
    element.click()
    time.sleep(5)
    element.click()
except TimeoutException:
    print(f"Element with CSS selector not found. Skipping to the next.")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@title='Unassigned'][normalize-space()='Unassigned'])[2]"))
    )
    element.click()
    time.sleep(5)
    element.click()
except TimeoutException:
    print(f"Element with CSS selector not found. Skipping to the next.")

###################     Directory #####################################
driver.find_element(By.LINK_TEXT, "Directory").click()
direct = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Directory"))
)
direct.click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@placeholder='Type for hints...']").send_keys("pet")
time.sleep(5)
a = driver.find_elements(By.CLASS_NAME, "oxd-autocomplete-option")
for i in a:
    if i.text == "Peter Mac Anderson":
        i.click()
sub = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Search']"))
)
sub.click()
time.sleep(3)
reset = driver.find_element(By.CSS_SELECTOR, "button[type='reset']")
reset.click()
time.sleep(3)
job = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'-- Select --')])[1]"))
)
job.click()
time.sleep(5)
automation_tester = driver.find_element(By.XPATH, "//span[text()='Automaton Tester']").click()
time.sleep(3)
sub.click()
try:
    no_records_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='No Records Found']"))
    )
    print("Message Displayed:", no_records_message.text)  # Print the message
except:
    print("No 'No Records Found' message displayed.")

time.sleep(2)
reset.click()
time.sleep(3)

location = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'-- Select --')])[2]"))
)
location.click()
time.sleep(5)
new_york = driver.find_element(By.XPATH, "//span[text()='New York Sales Office']").click()
time.sleep(3)
sub.click()
try:
    no_records_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='No Records Found']"))
    )
    print("Message Displayed:", no_records_message.text)  # Print the message
except:
    print("Record found")

time.sleep(2)
reset.click()
time.sleep(3)
