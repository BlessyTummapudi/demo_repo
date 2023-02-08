import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestAmazon:
    @pytest.fixture
    def driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        request.addfinalizer(driver.quit)
        return driver
    def test_login(self, driver):
        driver.get("https://www.amazon.in/amazonpay/home")
        driver.find_element(By.XPATH, "//span[text()='Hello, sign in']").click()
        driver.find_element(By.NAME, "email").send_keys("6301752050")
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        driver.find_element(By.NAME, "password").send_keys("Blessy@123")
        driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
        return driver
    def test_ticket(self, driver):
        driver.get("https://www.amazon.in/amazonpay/home")
        driver.find_element(By.XPATH, "//span[text()='Hello, sign in']").click()
        driver.find_element(By.NAME, "email").send_keys("6301752050")
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        driver.find_element(By.NAME, "password").send_keys("Blessy@123")
        driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
        driver.find_element(By.XPATH, "//span[text()='Flights']").click()
        driver.find_element(By.XPATH, "//button[text()='Search']").click()
        driver.find_element(By.XPATH, "//button[text()='Book']").click()
        driver.find_element(By.LINK_TEXT, "Proceed to traveller details").click()
        driver.find_element(By.XPATH, "//div[text()='Add new adult']").click()
        driver.find_element(By.XPATH, "//button[text()='Select']").click()
        driver.find_element(By.XPATH, "//li[text()='Ms']").click()
        driver.find_element(By.ID, "input-firstName").send_keys("blessy")
        driver.find_element(By.NAME, "lastName").send_keys("blsy")
        driver.find_element(By.XPATH, "//button[text()='Add adult']").click()
        driver.find_element(By.XPATH, "//i[@class='d726bd8f _4d2636f0']").click()
        driver.find_element(By.NAME, "communication_email").send_keys("blessy.tummapudi@gmail.com")
        driver.find_element(By.XPATH, "//button[normalize-space()='Proceed to review']").click()
        driver.find_element(By.XPATH, "//i[@class='d726bd8f _4d2636f0']").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='Proceed to Payment']").click()
        driver.find_element(By.XPATH, "//input[@name='ppw-instrumentRowSelection']").click()
        driver.find_element(By.XPATH, "//input[@name='ppw-widgetEvent:AddCreditCardEvent']").click()
        expected_header = 'Card number is required.\nExpiration date is not correct.'
        element = driver.find_element(By.XPATH, "//div[contains(@class,'a-alert-content')]")
        assert expected_header in element.text


