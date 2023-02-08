from selenium import webdriver
from selenium.webdriver.common.by import By

class Amazon:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.in/amazonpay/home")

    def login(self):
        self.driver.find_element(By.XPATH, "//span[text()='Hello, sign in']").click()
        self.driver.find_element(By.NAME, "email").send_keys("6301752050")
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        self.driver.find_element(By.NAME, "password").send_keys("Blessy@123")
        self.driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()

class Bookticket(Amazon):
    def ticket(self):
        self.driver.find_element(By.XPATH, "//span[text()='Flights']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Search']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Book']").click()
        self.driver.find_element(By.LINK_TEXT, "Proceed to traveller details").click()
        self.driver.find_element(By.XPATH, "//div[text()='Add new adult']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Select']").click()
        self.driver.find_element(By.XPATH, "//li[text()='Ms']").click()
        self.driver.find_element(By.ID, "input-firstName").send_keys("blessy")
        self.driver.find_element(By.NAME, "lastName").send_keys("blsy")
        self.driver.find_element(By.XPATH, "//button[text()='Add adult']").click()
        self.driver.find_element(By.XPATH, "//i[@class='d726bd8f _4d2636f0']").click()
        self.driver.find_element(By.NAME, "communication_email").send_keys("blessy.tummapudi@gmail.com")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed to review']").click()
        self.driver.find_element(By.XPATH, "//i[@class='d726bd8f _4d2636f0']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed to Payment']").click()
        self.driver.find_element(By.XPATH, "//input[@name='ppw-instrumentRowSelection']").click()
        self.driver.find_element(By.XPATH, "//input[@name='ppw-widgetEvent:AddCreditCardEvent']").click()

    def ele(self):
        try:
            self.driver.find_element(By.XPATH, "//span[text()='Hello, sign innn']").click()

        except:
            print("Invalid xpath")

obj = Bookticket()

def test_login():
    obj.login()
    assert obj.driver.title == "Amazon Sign In"

def test_ticket():
    obj.ticket()
    assert obj.driver.title == "Amazon Pay India"