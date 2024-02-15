from selenium import webdriver
from selenium.common import NoSuchElementException
import pytest

from pynput.keyboard import Key, Controller
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture()
def test_setupforservicerequest():
    global driver
    import time
    global time
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    global By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)

def test_servicrequestenegative(test_setupforservicerequest):
    driver.get("https://www.devpropvivo.com")
    time.sleep(10)

    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    try:
        emailfield = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html[1]/body[1]/app-root[1]/app-login[1]/div[1]/div[1]/div[2]/form[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)

    time.sleep(3)

    Email_box = driver.find_element(by=By.ID, value="mat-input-0")
    Email_box.send_keys("vipulkadam.vk9@gmail.com")
    time.sleep(1)
    Password_box = driver.find_element(by=By.ID, value="mat-input-1")
    Password_box.send_keys("Vipul@123")
    time.sleep(2)
    Login_button = driver.find_element(by=By.CSS_SELECTOR,
                                       value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
    Login_button.click()
    time.sleep(10)
    try:
        create = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//body//app-root//header//ul//a[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:
        # Error handling if success message doesn't appear within the specified time
        print("Form submission failed:", e)

    # You can also validate by checking for errors on the form
    # For example, if there's an error message displayed for invalid input
    try:
        error_message = driver.find_element(By.ID, 'error_message')
        print("Error occurred:", error_message.text)
    except NoSuchElementException:
        print("No errors detected. Form submitted successfully!")
    driver.maximize_window()
    time.sleep(2)

    driver.implicitly_wait(5)

    time.sleep(2)

    association= driver.find_element(by=By.XPATH, value="//a[@href='/association/association-list']")
    association.click()

    time.sleep(2)


    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-association-list/div/div[3]")
    time.sleep(2)


    GLA= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-association-list[1]/div[1]/div[3]/div[2]/table[1]/tbody[5]/tr[1]/td[2]/a[1]")
    GLA.click()

    time.sleep(2)

    target_elementoneo = driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-association-details[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/app-property-inspections-setting[1]/div[1]/div[3]/div[2]/div[1]/span[1]")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementoneo)


    #section= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-association-details[1]/div[1]/div[2]/ul[1]/li[2]/a[1]")
    #section.click()
    time.sleep(2)

    target_elementoneo = driver.find_element(by=By.XPATH,
                                             value="//app-association-relation-update//div//div//div//div[1]//span[1]")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementoneo)









