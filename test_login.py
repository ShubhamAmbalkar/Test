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

    # Navigate to the Entrata Login website
    driver.get("https://sso.entrata.com/entrata/login")
    
    yield driver

    # Close browser after test case
    driver.close()

class Test_Login_Entara:
    def test_login(self,test_setup):
        # Assert that Username text field is present
        username = driver.find_element(By.XPATH,'//input[contains(@id,"entrata-username")]')
        assert username.is_displayed()
        # Enter username in text field
        username = driver.find_element(By.XPATH,'//input[contains(@id,"entrata-username")]')
        username.send_keys("Shubham")

        # Assert that Username text field is present
        password = driver.find_element(By.XPATH,'//input[contains(@id,"entrata-password")]')
        assert password.is_displayed()

        # Enter username in text field
        password = driver.find_element(By.XPATH,'//input[contains(@id,"entrata-password")]')
        password.send_keys("Shubham")



