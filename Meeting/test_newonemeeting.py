from selenium import webdriver
from selenium.common import NoSuchElementException
import pytest

from pynput.keyboard import Key, Controller
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture()
def test_setupformeeting():
    global driver
    import time
    global time
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    global By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)

def test_meetingnegative(test_setupformeeting):
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
    Meeting_button = driver.find_element(by=By.XPATH, value="//a[@href='/association/pm-meeting']")
    Meeting_button.click()
    time.sleep(8)
    Add_button = driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-meeting[1]/div[1]/div[1]/div[2]/button[1]")
    Add_button.click()
    time.sleep(3)

    driver.find_element(by=By.XPATH, value="//div[@class='pv-meeting-wrap ng-star-inserted']")
    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-meeting/div/div/div/div[2]/div[1]")

    target_elementascancelbutton = driver.find_element(by=By.XPATH,
                                         value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-meeting[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[4]/button[2]")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementascancelbutton)
    time.sleep(5)


    Shedulemeeting_button = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    Shedulemeeting_button.click()
    time.sleep(3)

def test_meetingpositive(test_setupformeeting):
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
    Meeting_button = driver.find_element(by=By.XPATH, value="//a[@href='/association/pm-meeting']//span")
    Meeting_button.click()
    time.sleep(10)
    Add_button= driver.find_element(by=By.XPATH, value="//button[@class='mat-tooltip-trigger btn btn-orange']//i[@class='material-icons']")
    Add_button.click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//div[@class='pv-meeting-wrap ng-star-inserted']")
    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-meeting/div/div/div/div[2]/div[1]")

    Selectassociation_dropdown = driver.find_element(by=By.XPATH,
                                                     value="//input[@formcontrolname='association']")
    Selectassociation_dropdown.click()
    time.sleep(2)
    Selectassociationoptionlist = driver.find_element(by=By.XPATH,
                                                      value="//body/div[@class='cdk-overlay-container']/div[@class='cdk-overlay-connected-position-bounding-box']/div[@class='cdk-overlay-pane']/div[@role='listbox']/mat-option[17]/span[1]")
    Selectassociationoptionlist.click()
    time.sleep(3)
    Meetingtitle_box = driver.find_element(by=By.XPATH,
                                           value="//body/app-root/app-main/app-pm-meeting/div/div/div/div/div/form/div/div/div[2]/div[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]")
    Meetingtitle_box.send_keys("Demo meeting for script writing")
    time.sleep(3)
    Meetingtype_dropdown = driver.find_element(by=By.XPATH,
                                               value="//body/app-root/app-main/app-pm-meeting/div/div/div/div/div/form/div/div/div/div/div/mat-form-field/div/div/div/mat-select[@placeholder='Meeting Type']/div/div[1]")
    Meetingtype_dropdown.click()
    time.sleep(4)
    Meetingtypelist = driver.find_element(by=By.XPATH, value="//mat-option[1]//span[1]")
    Meetingtypelist.click()
    time.sleep(4)
    Startdatetime = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='startDateTime']")
    Startdatetime.click()
    time.sleep(2)
    date = driver.find_element(by=By.XPATH, value="//td[@aria-label='December 1, 2023']//div[@class='mat-datetimepicker-calendar-body-cell-content']")
    date.click()
    time.sleep(5)

    # Timepickerframe = driver.find_element(by=By.XPATH, value="//body/div/div[@dir='ltr']/div/mat-datetimepicker-content/mat-datetimepicker-calendar[@aria-label='Use arrow keys to navigate']/div[2]")
    timepicker = driver.find_element(by=By.XPATH,
                                     value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[3]/div[7]")
    timepicker.click()
    time.sleep(2)
    timepickermin = driver.find_element(by=By.XPATH,
                                        value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[4]/div[7]")
    timepickermin.click()
    time.sleep(3)
    enddatetime = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='endDateTime']")
    enddatetime.click()
    enddate = driver.find_element(by=By.XPATH,
                                  value="//td[@aria-label='December 1, 2023']//div[@class='mat-datetimepicker-calendar-body-cell-content']")
    enddate.click()
    time.sleep(3)
    enddatetimepicker = driver.find_element(by=By.XPATH,
                                            value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[3]/div[9]")
    enddatetimepicker.click()
    time.sleep(3)
    enddatetimepickermin = driver.find_element(by=By.XPATH,
                                               value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[4]/div[7]")
    enddatetimepickermin.click()
    time.sleep(3)
    audiencetype = driver.find_element(by=By.XPATH,
                                       value="//body/app-root/app-main/app-pm-meeting/div/div/div/div/div/form/div/div/div/div/div/mat-form-field/div/div/div/mat-select[@placeholder='Audience Type']/div/div[1]")
    audiencetype.click()
    time.sleep(3)
    audiencelist = driver.find_element(by=By.XPATH,
                                       value="//mat-option[@value='false']//span[@class='mat-option-text']")
    audiencelist.click()
    time.sleep(3)
    Meetinglocation_box = driver.find_element(by=By.XPATH,
                                              value="//body/app-root/app-main/app-pm-meeting/div/div/div/div/div/form/div/div/div/div/div[2]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]")
    Meetinglocation_box.send_keys("Garden")
    time.sleep(3)
    Newagendapoint_box = driver.find_element(by=By.XPATH,
                                             value="//body//app-root//app-main//app-pm-meeting//div//div//div//div//div//form//div//div//div//div//form//div//div//div//mat-form-field//div//div//div//input[@autocomplete='off']")
    Newagendapoint_box.send_keys("Test agenda")
    time.sleep(2)
    Agendadescription_box = driver.find_element(by=By.XPATH,
                                                value="//body//app-root//app-main//app-pm-meeting//div//div//div//div//div//form//div//div//div//div//form//div//div//div//mat-form-field//div//div//div//textarea")
    Agendadescription_box.send_keys("Test")
    time.sleep(3)
    Addagendabutton_button = driver.find_element(by=By.XPATH,
                                                 value="//body/app-root/app-main/app-pm-meeting/div/div/div/div/div/form/div/div/div/div/div/button[1]")
    Addagendabutton_button.click()
    time.sleep(3)
    target_elementascancelbutton = driver.find_element(by=By.XPATH,
                                                       value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-meeting[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[4]/button[2]")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementascancelbutton)
    Shedulemeeting_button = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    Shedulemeeting_button.click()
    time.sleep(3)


def test_meetingBM(test_setupformeeting):
    driver.get("https://www.devpropvivo.com")
    time.sleep(3)
    windowID = driver.current_window_handle
    print(windowID)  # 993C69FDDE85F986A01BA3D388B14376
    time.sleep(3)

    driver.switch_to.window(windowID)
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
    Email_box.send_keys("yash.bmtekgrid@gmail.com")
    time.sleep(2)
    Password_box = driver.find_element(by=By.ID, value="mat-input-1")
    Password_box.send_keys("Abcd123#")
    time.sleep(2)
    Login_button = driver.find_element(by=By.CSS_SELECTOR,
                                       value="body > app-root > app-login > div > div > div.col-md-6.login-form-cotainer > form > button")
    Login_button.click()
    time.sleep(10)
    driver.implicitly_wait(5)