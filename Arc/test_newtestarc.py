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


    Arcapproval= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-header[1]/nav[1]/div[1]/div[7]/div[2]/div[4]/div[1]/ul[1]/li[1]/a[1]")
    Arcapproval.click()

    try:
        create = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//tbody/tr[1]/td[1]/a[1]/span[1]/span[1]/span[2]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)


    try:
        error_message = driver.find_element(By.ID, 'error_message')
        print("Error occurred:", error_message.text)
    except NoSuchElementException:
        print("No errors detected. Form submitted successfully!")


    driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-pm-arc-list")


    Addform= driver.find_element(by=By.XPATH, value="//button[@color='primary']")
    Addform.click()

    time.sleep(2)

    Associationdropdown= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-create-arc[1]/div[1]/div[1]/div[2]/app-association-dropdown[1]/div[1]/div[1]/form[1]/input[1]")
    Associationdropdown.click()

    Asslist= driver.find_element(by=By.XPATH,value="/html/body/div[5]/div/div/div/mat-option[9]/span")
    Asslist.click()


    try:
        create = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//body/app-root/app-main/app-pm-create-arc/div/div/div/div/div/div[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)


    try:
        error_message = driver.find_element(By.ID, 'error_message')
        print("Error occurred:", error_message.text)
    except NoSuchElementException:
        print("No errors detected. Form submitted successfully!")


    Createarcapproval= driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-create-arc/div/div/div/div/a[2]")
    Createarcapproval.click()


    try:
        create = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//body/app-root/app-main/app-pm-create-arc/app-arc-guideline-preview/div/div/div/mat-checkbox/label[@for="mat-checkbox-1-input"]/span[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)


    try:
        error_message = driver.find_element(By.ID, 'error_message')
        print("Error occurred:", error_message.text)
    except NoSuchElementException:
        print("No errors detected. Form submitted successfully!")

    checkbox = driver.find_element(by=By.XPATH,
                                   value="//body/app-root/app-main/app-pm-create-arc/app-arc-guideline-preview/div/div/div/mat-checkbox/label[@for='mat-checkbox-1-input']/span[1]")
    time.sleep(2)
    if not checkbox.is_selected():
        # If the checkbox is not selected, click it to select
        checkbox.click()

    Confirmbutton= driver.find_element(by=By.XPATH, value="//body//app-root//app-arc-guideline-preview//button[2]")
    Confirmbutton.click()


    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-create-arc/div/div/div[2]")

    Selectassociationone= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-create-arc[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]")
    Selectassociationone.click()

    listaone= driver.find_element(by=By.XPATH, value="//mat-option[1]//span[1]//span[1]")
    listaone.click()
    time.sleep(2)

    Selectmember= driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-create-arc/div/div/div/form[@name='frmCreateARCRequest']/div/div/div[3]/mat-form-field[1]/div[1]/div[1]/div[1]" )
    Selectmember.click()

    time.sleep(2)

    member= driver.find_element(by=By.XPATH, value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[@role='option']/span[1]")
    member.click()

    Title= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='title']")
    Title.send_keys("Test new")

    Startdate= driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-pm-create-arc/div[1]/div/div[2]/form/div[2]/div/div[2]/div/div[1]")
    Startdate.click()

    time.sleep(1)
    forwardbutton= driver.find_element(by=By.XPATH, value="//button[@aria-label='Next month']")
    forwardbutton.click()
    time.sleep(1)

    firstdate = driver.find_element(by=By.XPATH, value="//td[@aria-label='March 1, 2024']//div[1]")
    firstdate.click()
    time.sleep(1)

    Enddate=driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-pm-create-arc/div[1]/div/div[2]/form/div[2]/div/div[2]/div/div[2]")
    Enddate.click()
    time.sleep(1)

    forwardbuttononeone=driver.find_element(by=By.XPATH, value="//button[@aria-label='Next month']")
    forwardbuttononeone.click()
    time.sleep(2)
    forwardbuttononeonetwo= driver.find_element(by=By.XPATH, value="//button[@aria-label='Next month']")
    forwardbuttononeonetwo.click()
    time.sleep(2)

    endfirstdate= driver.find_element(by=By.XPATH, value="//td[@aria-label='April 1, 2024']//div[1]")
    endfirstdate.click()



    Estimatedcost=driver.find_element(by=By.XPATH, value="//input[@formcontrolname='cost']")
    Estimatedcost.send_keys("100")

    time.sleep(1)

    Assignto= driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-create-arc/div/div/div/form[@name='frmCreateARCRequest']/div/div/div/mat-form-field/div/div/div/mat-select[@placeholder='Select Assign To']/div/div[1]")
    Assignto.click()
    time.sleep(1)

    ArjunPM= driver.find_element(by=By.XPATH, value="//mat-option[4]//span[1]")
    ArjunPM.click()
    time.sleep(1)
    Adddescription= driver.find_element(by=By.XPATH, value="//div[4]//div[1]//div[1]//mat-form-field[1]//div[1]//div[1]//div[1]")
    Adddescription.click()

    time.sleep(2)
    file_input = driver.find_element(by=By.XPATH,
                                     value="//body/app-root/app-main/app-pm-create-arc/div/div/div/form[@name='frmCreateARCRequest']/div/div/div/div/button[1]")
    file_input.click()
    time.sleep(5)
    keyboard = Controller()
    keyboard.type("file:///C:/Users/PVlap/OneDrive/Documents/Pvscaninvoice.pdf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)

    checkbox = driver.find_element(by=By.XPATH,
                                   value="//body/app-root/app-main/app-pm-create-arc/div/div/div/form[@name='frmCreateARCRequest']/div/mat-checkbox[@formcontrolname='isMarkAllUploadedDocument']/label[@for='mat-checkbox-10-input']/span[1]")
    if not checkbox.is_selected():
        # If the checkbox is not selected, click it to select
        checkbox.click()


    Submitbutton= driver.find_element(by=By.XPATH, value="//form[@name='frmCreateARCRequest']//div//div//div//button[@type='submit']")
    Submitbutton.click()

    time.sleep(2)







































