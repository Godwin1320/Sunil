import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class Directory:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 13)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def search_by_name(self, sen, text1):
        direct = (By.LINK_TEXT, "Directory")
        name_locator = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
        dropdown1 = (By.CLASS_NAME, "oxd-autocomplete-option")

        try:
            self.wait_for_element(direct).click()
            name_input = self.wait_for_element(name_locator)
            name_input.send_keys(sen)
            time.sleep(2)
            drop = self.driver.find_elements(*dropdown1)
            time.sleep(5)
            for i in drop:
                if i.text == text1:   #"Peter Mac Anderson"
                    i.click()
                    time.sleep(4)
                else:
                    print("No Records Found")

        except Exception as e:
            print(f"Error during name search: {e}")

        return self

    def search(self):
        search_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        clear_button_locator = (By.CSS_SELECTOR, "button[type='reset']")

        search_button = self.wait_for_element(search_button_locator)
        search_button.click()
        time.sleep(5)

        clear_button = self.wait_for_element(clear_button_locator)
        clear_button.click()
        time.sleep(2)  # Wait for the page to resets

    def filter_by_job_title(self, title):
        job_title_locator = (By.XPATH, "//div[contains(text(),'-- Select --')][1]")
        automation = (By.XPATH, f"//span[text()='{title}']")
        search_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        clear_button_locator = (By.CSS_SELECTOR, "button[type='reset']")

        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(job_title_locator)).click()
            automation_tester = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(automation))
            automation_tester.click()
            search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(search_button_locator))
            search_button.click()

            try:
                no_records_message = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='No Records Found']"))
                )
                print("Message Displayed:", no_records_message.text)
            except:
                print("Records Found message displayed.")

            clear_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(clear_button_locator))
            clear_button.click()
        except Exception as e:
            print(f"Error during job title filtering: {e}")
        return self

    def filter_by_location(self, location):
        location_locator = (By.XPATH, "(//div[contains(text(),'-- Select --')])[2]")
        location_option = (By.XPATH, f"//span[normalize-space()='{location}']")
        # location_option = (By.XPATH, "//span[normalize-space()='New York Sales Office']")
        search_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        clear_button_locator = (By.CSS_SELECTOR, "button[type='reset']")

        try:
            # Wait and click the location dropdown
            location_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(location_locator)
            )
            location_dropdown.click()
            time.sleep(4)

            # Wait and click the desired location option
            location_option_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(location_option)
            )
            location_option_element.click()
            time.sleep(4)
            # Wait and click the search button
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(search_button_locator)
            )
            search_button.click()
            time.sleep(4)
            # Wait and click the clear button
            clear_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(clear_button_locator)
            )
            clear_button.click()
            time.sleep(4)

        except Exception as e:
            print(f"Error during location filtering: {e}")

        return self
