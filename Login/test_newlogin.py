import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
@pytest.fixture()
def testsetup_n_teardown():
    global driver
    import time
    global time
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)



def testlogedinbyinvalidinpute(testsetup_n_teardown):
    import time
    driver.get("https://www.devpropvivo.com")
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(3)

    Email_box = driver.find_element(by=By.ID, value="mat-input-0")
    Email_box.send_keys("test")
    time.sleep(1)
    Password_box = driver.find_element(by=By.ID, value="mat-input-1")
    Password_box.send_keys("testone")
    time.sleep(1)
    Login_button = driver.find_element(by=By.CSS_SELECTOR,
                                       value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
    Login_button.click()
    time.sleep(10)

def testlogedinbyemptyinpute(testsetup_n_teardown):
    import time
    driver.get("https://www.devpropvivo.com")
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(3)

    Email_box = driver.find_element(by=By.ID, value="mat-input-0")
    Email_box.send_keys("")
    time.sleep(1)
    Password_box = driver.find_element(by=By.ID, value="mat-input-1")
    Password_box.send_keys("")
    time.sleep(1)
    Login_button = driver.find_element(by=By.CSS_SELECTOR,
                                       value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
    Login_button.click()
    time.sleep(10)


def testlogedinbyaddonefieldandoneempty(testsetup_n_teardown):


    driver.get("https://www.devpropvivo.com")
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(3)

    Email_box = driver.find_element(by=By.ID, value="mat-input-0")
    Email_box.send_keys("vipulkadam.vk9@gmail.com")
    time.sleep(1)
    Password_box = driver.find_element(by=By.ID, value="mat-input-1")
    Password_box.send_keys("")
    time.sleep(1)
    Login_button = driver.find_element(by=By.CSS_SELECTOR,
                                       value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
    Login_button.click()
    time.sleep(10)