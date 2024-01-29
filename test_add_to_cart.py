import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Fixture to set up the WebDriver instance
@pytest.fixture()
def test_setup():
    global driver
    # Initialize the WebDriver (Edge in this case)
    driver = webdriver.Edge()
    # Navigate to the Saucedemo website
    driver.get('https://www.saucedemo.com')
    # Yield the driver to the test function
    yield driver
    # Close the browser after the test
    driver.close()

# Test class for checking email box visibility
class Test_EmailBox_001:
    def test_email_box_visibility(self, test_setup):
        # Navigate to the website again to ensure a clean state
        driver.get('https://www.saucedemo.com')
        # Find the email input box by XPath
        inputBoxEmail = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        # Check if the email input box is displayed
        assert inputBoxEmail.is_displayed()

# Test class for login functionality
class Test_Login_002:
    # Valid Login Test
    def test_validLogin(self, test_setup):
        # Clear the username field
        driver.find_element(By.XPATH, '//*[@id="user-name"]').clear()
        # Enter a valid username
        enter_username('stazndard_user')
        # Clear the password field
        driver.find_element(By.XPATH, '//*[@id="password"]').clear()
        # Enter a valid password
        enter_password('secret_sauce')
        # Click the login button
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        # Check if the success message is displayed
        if driver.title == "Swag Labs":
            assert True
        else:
            assert False

    # Invalid Login Test
    def test_invalidLogin(self, test_setup):
        # Clear the username field
        driver.find_element(By.XPATH, '//*[@id="user-name"]').clear()
        # Enter an invalid username
        enter_username('standard_user')
        # Clear the password field
        driver.find_element(By.XPATH, '//*[@id="password"]').clear()
        # Enter an invalid password
        enter_password('secret_auce')
        # Click the login button
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        # Check if the error message is displayed
        if driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').is_displayed():
            print("Invalid login failed.")
            assert True
        else:
            assert False

# Test class for adding items to the cart
class Test_AddToCart_003:
       def test_addtocart(self, test_setup):
        # Placeholder: Navigate to a product, add it to the cart, and verify successful addition

        # Clear the username field
        driver.find_element(By.XPATH, '//*[@id="user-name"]').clear()
        # Enter a valid username
        enter_username('standard_user')
        # Clear the password field
        driver.find_element(By.XPATH, '//*[@id="password"]').clear()
        # Enter a valid password
        enter_password('secret_sauce')
        # Click the login button
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Navigate to a product page (replace '//*[@id="item_4_title_link"]/div' with the actual XPath)
        driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()

        # Add the product to the cart (replace '//*[@id="add-to-cart-sauce-labs-backpack"]' with the actual XPath)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

        # View the shopping cart (replace '//*[@id="shopping_cart_container"]/a' with the actual XPath)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        # Placeholder for verification, replace with your actual verification logic
        assert driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').is_displayed()

# Test class for sorting items
class Test_sort_item_004:
   
    def test_sorting_items(self, test_setup):
        # Placeholder: Sort items and verify the order

        # Navigate to the inventory page
        driver.get("https://www.saucedemo.com/inventory.html")
        # Clear the username field
        driver.find_element(By.XPATH, '//*[@id="user-name"]').clear()
        # Enter a valid username
        enter_username('standard_user')
        # Clear the password field
        driver.find_element(By.XPATH, '//*[@id="password"]').clear()
        # Enter a valid password
        enter_password('secret_sauce')
        # Click the login button
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Select sorting option from the dropdown
        sort_dropdown = driver.find_element(By.CSS_SELECTOR, 'select[data-test="product_sort_container"]')
        sort_dropdown.click()

        # Select the second option (name Z to A) for sorting
        sort_options = driver.find_elements(By.CSS_SELECTOR, 'select[data-test="product_sort_container"] option')
        sort_options[1].click()

        # Get the names of the sorted products
        products = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_name')
        sorted_product_names = [p.text for p in products]

        # Define the expected order of product names after sorting
        expected_order = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket',
                          'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']

        # Verify if the products are sorted in the expected order
        assert sorted_product_names == expected_order

    # Step function for entering username
def enter_username(Username):
    # Find the username input field by XPath
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(Username)

# Step function for entering password
def enter_password(Password):
    # Find the password input field by XPath
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Password)
