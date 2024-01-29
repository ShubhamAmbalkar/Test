import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup():
    global driver
     # Initialize the Chrome driver
    driver = webdriver.Edge()

    # Navigate to the Entrata website
    driver.get("https://www.entrata.com/")
    
    yield driver

    # Close browser after test case
    driver.close()

class Test_Navigation:
    def test_navigation(self,test_setup):
   
        # Wait for the home page to load
        home_page = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(@title, "Entrata Home Page")]'))
        )

        # Get the initial title
        initial_title = driver.title

        # Click on the 'Resources' link
        resources_xpath = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div[3]/a")
        resources_xpath.click()

        # Wait for the about page to load
        resource_page = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[contains(text(), "Resource Center")]'))
        )

        # Get the page title after clicking on the 'Resources' link
        next_title = driver.title

        # Assert that the page title has changed
        assert initial_title != next_title
    
        # Click on the browser back button
        driver.back()
        # Wait for the home page to load again
        home_page = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(@title, "Entrata Home Page")]'))
        )

        # Get the page title after clicking the back button
        back_button_title = driver.title

        # Assert that the page title is the same as the initial page title
        assert back_button_title == initial_title

       