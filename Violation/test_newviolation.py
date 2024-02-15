from selenium import webdriver
from selenium.common import NoSuchElementException
import pytest

from pynput.keyboard import Key, Controller
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture()
def test_Setup():
    global driver
    import time
    global time
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    global By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)

def test_negativevolation(test_Setup):
    driver.get("https://www.devpropvivo.com")
    try:
        emailfield = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html[1]/body[1]/div[2]/div[1]/div[3]/ul[1]/li[7]/a[1]'))
        )
        print("Loging button successfully!")
    except Exception as e:

        print("Visibility failed:", e)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    try:
        emailfield = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html[1]/body[1]/app-root[1]/app-login[1]/div[1]/div[1]/div[2]/form[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)

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

        print("Form submission failed:", e)


    try:
        error_message = driver.find_element(By.ID, 'error_message')
        print("Error occurred:", error_message.text)
    except NoSuchElementException:
        print("No errors detected. Form submitted successfully!")


    driver.maximize_window()

    Manageassociation= driver.find_element(by=By.XPATH, value="//span[normalize-space()='Manage Association']")
    Manageassociation.click()
    time.sleep(1)
    Violation= driver.find_element(by=By.XPATH, value="//a[normalize-space()='Violations Report']")
    Violation.click()




    try:
        emailfield = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//body/app-root/app-main/app-pm-violation-list/div/div/div/div/div[1]'))
        )
        print("element visible successfully!")
    except Exception as e:

        print("Form submission failed:", e)




    Plusebutton= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-violation-list[1]/div[1]/div[1]/div[2]/button[1]/span[1]/i[1]")
    Plusebutton.click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,  value="//body/app-root/app-main/app-pm-violation-list/div[3]")

    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-violation-list/div[3]/div[2]")


    Associationdropdown= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-violation-list[1]/div[3]/div[2]/form[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]")
    Associationdropdown.click()
    time.sleep(1)
    Namelist= driver.find_element(by=By.XPATH, value="//mat-option[9]//span[1]//span[1]")
    Namelist.click()
    time.sleep(2)
    Violatedby= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='violatedByAssociationUnit']")
    Violatedby.click()
    time.sleep(3)
    Violatedbylist= driver.find_element(by=By.XPATH, value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[1]/span[1]")
    Violatedbylist.click()
    time.sleep(1)

    Violationdate= driver.find_element(by=By.XPATH,value="//input[@readonly='true']")
    Violationdate.click()
    Dateone= driver.find_element(by=By.XPATH,value="//td[@aria-label='January 1, 2024']//div[1]")
    Dateone.click()
    time.sleep(2)

    Reportedby= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='reportedByUser']")
    Reportedby.click()
    time.sleep(1)
    listone= driver.find_element(by=By.XPATH, value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[1]/span[1]")
    listone.click()
    time.sleep(1)

    Title= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='title']")
    Title.send_keys("New violation for auto script")
    time.sleep(1)

    Description=driver.find_element(by=By.XPATH, value="//textarea[@formcontrolname='description']")
    Description.send_keys("Test violation script")
    time.sleep(1)

    Addbutton= driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-violation-list/div/div/form[@name='frmCreateViolation']/div/button[1]")
    Addbutton.click()
    time.sleep(4)

    try:
        emailfield = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//body//app-root//div//div//div//div//div[1]//div[1]//div[2]//div[3]//button[1]'))
        )
        print("element is visible successfully!")
    except Exception as e:

        print("Form submission failed:", e)

    driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-pm-violation-list/div[1]")

    Selectccrtype= driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-violation-list/div/div/div/div/div[1]/div[1]/div[2]/div[2]/mat-select[1]/div[1]/div[1]")
    Selectccrtype.click()

    ccrtypelist= driver.find_element(by=By.XPATH, value="//mat-option[2]//span[1]")
    ccrtypelist.click()



    Approve= driver.find_element(by=By.XPATH, value="//body//app-root//div//div//div//div//div[1]//div[1]//div[2]//div[3]//button[1]")
    Approve.click()
