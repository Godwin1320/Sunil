import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class DashBoard:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 13)  # Wait up to 10 seconds

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def time_at_work(self):
        locator = (By.XPATH, "(//i[@class='oxd-icon bi-stopwatch'])[1]")
        element = self.driver.find_element(*locator)
        element.click()  # Click the element
        time.sleep(5)
        self.driver.back()  # Go back
        time.sleep(5)
        return self

    def my_actions(self):
        locators = [
            (By.CSS_SELECTOR, "div[class='orangehrm-todo-list-item'] p[class='oxd-text oxd-text--p']"),
            (By.XPATH, "//p[normalize-space()='(1) Candidate to Interview']"),
            (By.XPATH, "//p[normalize-space()='(1) Pending Self Review']")
        ]
        elements = []
        for locator in locators:
            try:
                element = self.driver.find_element(*locator)
                elements.append(element)  # Add found element to the list
                element.click()  # Click the element
                time.sleep(5)
                self.driver.back()  # Go back
                time.sleep(5)
            except Exception as e:
                print(f"Element not found for locator {locator}: {e}")  # Log the exception and move on
        return elements

    def quick_launch(self):
        locators = [
            (By.CSS_SELECTOR, "button[title='Assign Leave'] svg"),
            (By.CSS_SELECTOR, "button[title='Leave List'] svg"),
            (By.CSS_SELECTOR, "button[title='Timesheets'] svg"),
            (By.CSS_SELECTOR, "button[title='Apply Leave'] svg"),
            (By.CSS_SELECTOR, "button[title='My Leave'] svg"),
            (By.CSS_SELECTOR, "button[title='My Timesheet'] svg")
        ]
        elements = []
        for locator in locators:
            try:
                element = self.wait_for_element(locator)
                elements.append(element)  # Add found element to the list
                element.click()
                time.sleep(5)
                self.driver.back()
                time.sleep(5)
            except Exception as e:
                print(f"Element not found for locator {locator}: {e}")
        return elements

    def buzz_latest(self):
        locator = (By.CSS_SELECTOR, ".orangehrm-buzz-widget-header")
        element = self.wait_for_element(locator)
        element.click()  # Click the element
        time.sleep(5)
        self.driver.back()  # Go back after clicking
        time.sleep(5)
        return element

    def employees_on_leave_today(self):
        locator1 = (By.XPATH, "//i[@class='oxd-icon bi-gear-fill orangehrm-leave-card-icon']")
        locator2 = (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        locator3 = (By.CSS_SELECTOR, "button[type='submit']")
        locator4 = (By.XPATH, "//button[normalize-space()='Cancel']")
        locator5 = (By.CSS_SELECTOR, ".oxd-dialog-close-button.oxd-dialog-close-button-position")

        element1 = self.wait.until(EC.visibility_of_element_located(locator1)).click()
        element2 = self.wait.until(EC.visibility_of_element_located(locator2))
        element3 = self.wait.until(EC.element_to_be_clickable(locator3))
        element4 = self.wait.until(EC.element_to_be_clickable(locator4))
        element5 = self.wait.until(EC.element_to_be_clickable(locator5))

        # element1.click()  # Click the element
        time.sleep(5)
        element2.click()  # Go back
        time.sleep(5)
        element3.click()
        time.sleep(5)
        element1 = self.wait.until(EC.visibility_of_element_located(locator1)).click()
        time.sleep(5)
        element4 = self.wait.until(EC.element_to_be_clickable(locator4)).click()
        time.sleep(5)
        element1 = self.wait.until(EC.visibility_of_element_located(locator1)).click()
        time.sleep(5)
        element5 = self.wait.until(EC.element_to_be_clickable(locator5)).click()
        time.sleep(5)
        return self

    def employees_distribution_sub_unit(self):
        locators = [
            (By.CSS_SELECTOR, "span[title='Engineering']"),
            (By.CSS_SELECTOR, "span[title='Human Resources']"),
            (By.CSS_SELECTOR, "span[title='Administration']"),
            (By.CSS_SELECTOR, "span[title='Client Services']"),
            (By.XPATH, "(//span[@title='Unassigned'][normalize-space()='Unassigned'])[1]")
        ]
        elements = []
        for locator in locators:
            try:
                element = self.driver.find_element(*locator)
                elements.append(element)  # Add found element to the list
                element.click()
                time.sleep(5)
                element.click()
                time.sleep(5)
            except Exception as e:
                print(f"Element not found for locator {locator}: {e}")  # Log the exception and move on

        return elements

    def employees_distribution_location(self):
        locators = [
            (By.CSS_SELECTOR, "span[title='Texas R&D']"),
            (By.CSS_SELECTOR, "span[title='New York Sales Office']"),
            (By.XPATH, "(//span[@title='Unassigned'][normalize-space()='Unassigned'])[2]")
        ]
        elements = []
        for locator in locators:
            try:
                # Use WebDriverWait to wait for the element to be present
                element = self.wait_for_element(locator)
                elements.append(element)
                element.click()
                time.sleep(5)
                element.click()
                time.sleep(5)
            except Exception as e:
                print(f"Element not found for locator {locator}: {e}")  # Log the exception and move on
        return elements
