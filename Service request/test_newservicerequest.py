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
    Manageassociation = driver.find_element(by=By.XPATH, value="//div[7]//div[1]//h5[1]//button[1]//span[1]")
    Manageassociation.click()
    time.sleep(5)
    Servicerequest = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Service Requests']")
    Servicerequest.click()
    time.sleep(11)
    driver.maximize_window()
    Pluse_button = driver.find_element(by=By.XPATH,
                                       value="//button[@class='mat-focus-indicator mat-tooltip-trigger btn btn-orange btn-add mat-flat-button mat-button-base mat-primary']")
    Pluse_button.click()
    time.sleep(4)
    driver.find_element(by=By.XPATH, value="//div[@class='pv-create-sidebar-wrap pv-active-sidebar']")
    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-service-request-list/div[3]/div[2]")
    time.sleep(1)


    target_element = driver.find_element(by=By.XPATH,
                                         value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-service-request-list[1]/div[3]/div[2]/form[1]/div[3]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_element)
    time.sleep(3)
    target_elementa = driver.find_element(by=By.XPATH,
                                          value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-service-request-list[1]/div[3]/div[2]/form[1]/div[8]/mat-form-field[1]/div[1]/div[1]/div[1]/mat-select[1]/div[1]/div[1]/span[1]")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementa)
    time.sleep(4)

    target_elementone = driver.find_element(by=By.XPATH, value="//button[@type='submit']")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementone)
    time.sleep(4)

    ADD_button = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    ADD_button.click()
    time.sleep(6)
    driver.maximize_window()


def test_servicerequestpositive(test_setupforservicerequest):
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
    Manageassociation = driver.find_element(by=By.XPATH, value="//div[7]//div[1]//h5[1]//button[1]//span[1]")
    Manageassociation.click()
    time.sleep(1)
    Servicerequest = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Service Requests']")
    Servicerequest.click()
    time.sleep(11)
    driver.maximize_window()
    Pluse_button = driver.find_element(by=By.XPATH,
                                       value="//button[@class='mat-focus-indicator mat-tooltip-trigger btn btn-orange btn-add mat-flat-button mat-button-base mat-primary']")
    Pluse_button.click()
    time.sleep(4)
    driver.find_element(by=By.XPATH, value="//div[@class='pv-create-sidebar-wrap pv-active-sidebar']")
    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pm-service-request-list/div[3]/div[2]")
    time.sleep(3)
    Formfield = driver.find_element(by=By.XPATH,
                                    value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]")
    Formfield.click()
    time.sleep(4)
    Dropdownlist = driver.find_element(by=By.XPATH,
                                       value="//span[@class='mat-option-text'][normalize-space()='Association']")
    Dropdownlist.click()
    time.sleep(3)
    Casetype = driver.find_element(by=By.XPATH,
                                   value="//body/app-root/app-main/app-pm-service-request-list/div/div/form/div[2]/div[1]/div[1]")
    Casetype.click()
    time.sleep(1)
    Casetypelist = driver.find_element(by=By.XPATH, value="//mat-option[1]//span[1]")
    Casetypelist.click()
    time.sleep(1)
    Casetopic = driver.find_element(by=By.XPATH,
                                    value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div[2]/div[1]/div[2]")
    Casetopic.click()
    time.sleep(1)
    Casetopiclist = driver.find_element(by=By.XPATH, value="//mat-option[3]//span[1]")
    Casetopiclist.click()
    time.sleep(1)
    target_element = driver.find_element(by=By.XPATH,
                                         value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-service-request-list[1]/div[3]/div[2]/form[1]/div[3]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_element)
    selectassociation = driver.find_element(by=By.XPATH,
                                            value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div[3]/mat-form-field[1]/div[1]/div[1]/div[1]")
    selectassociation.click()
    time.sleep(1)
    selectassociationlist = driver.find_element(by=By.XPATH,
                                                value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[9]/span[1]")
    selectassociationlist.click()
    time.sleep(1)
    associationunit = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='associationUnit']")
    associationunit.click()
    time.sleep(1)
    unitoption = driver.find_element(by=By.XPATH, value="//mat-option[1]//span[1]//span[1]")
    unitoption.click()
    time.sleep(1)
    target_elementa = driver.find_element(by=By.XPATH,
                                          value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-service-request-list[1]/div[3]/div[2]/form[1]/div[8]/mat-form-field[1]/div[1]/div[1]/div[1]/mat-select[1]/div[1]/div[1]/span[1]")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementa)
    time.sleep(4)

    selectmember = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='memberName']")
    selectmember.click()
    time.sleep(1)
    selectmemberlist = driver.find_element(by=By.XPATH,
                                           value="/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/mat-option[1]/span[1]")
    selectmemberlist.click()
    time.sleep(1)

    unitrole = driver.find_element(by=By.XPATH,
                                   value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div/mat-form-field/div/div/div/mat-select[@placeholder='Select Unit Role']/div/div[1]")
    unitrole.click()
    time.sleep(1)
    unitroleoption = driver.find_element(by=By.XPATH, value="//mat-option[1]//span[1]")
    unitroleoption.click()
    Caseoriginatingtype = driver.find_element(by=By.XPATH,
                                              value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div/mat-form-field/div/div/div/mat-select[@placeholder='Case Originating Type']/div/div[1]")
    Caseoriginatingtype.click()
    time.sleep(1)
    Caseoriginatingtypelist = driver.find_element(by=By.XPATH, value="//mat-option[1]//span[1]")
    Caseoriginatingtypelist.click()
    time.sleep(1)
    selectcategory = driver.find_element(by=By.XPATH,
                                         value="//mat-select[@placeholder='Select Category']//div//div//span")
    selectcategory.click()
    time.sleep(2)
    selectcategorylist = driver.find_element(by=By.XPATH, value="//mat-option[@role='option']//span")
    selectcategorylist.click()
    time.sleep(1)
    selectsubcategory = driver.find_element(by=By.XPATH,
                                            value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div/div/mat-form-field/div/div/div/mat-select[@placeholder='Select Sub Category']/div/div[1]")
    selectsubcategory.click()
    time.sleep(1)
    selectsubcategorylist = driver.find_element(by=By.XPATH, value="//span[@class='mat-option-text']")
    selectsubcategorylist.click()
    time.sleep(1)
    Addtitle = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='title']")
    Addtitle.send_keys("Test service request script 29date")
    time.sleep(1)
    target_elementone = driver.find_element(by=By.XPATH, value="//button[@type='submit']")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementone)
    time.sleep(4)
    Des = driver.find_element(by=By.XPATH, value="//textarea[@formcontrolname='comment']")
    Des.send_keys("test")
    time.sleep(1)

    Urgencylevel = driver.find_element(by=By.XPATH,
                                       value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div/div/div/mat-form-field/div/div/div/mat-select[@placeholder='Urgency Level']/div/div[1]")
    Urgencylevel.click()
    time.sleep(1)
    Urgencylevellist = driver.find_element(by=By.XPATH,
                                           value="//span[@class='mat-option-text'][normalize-space()='Medium']")
    Urgencylevellist.click()
    time.sleep(1)
    Selectassignto = driver.find_element(by=By.XPATH,
                                         value="//body/app-root/app-main/app-pm-service-request-list/div/div/form[@name='addRequestForm']/div[13]/mat-form-field[1]/div[1]")
    Selectassignto.click()
    time.sleep(1)
    Selectassigntolist = driver.find_element(by=By.XPATH, value="//mat-option[4]//span[1]")
    Selectassigntolist.click()
    time.sleep(1)
    date_input = driver.find_element(by=By.ID, value="mat-input-7")
    date_input.click()
    time.sleep(3)
    # desired_date = "2023-12-01"
    # year, month, day = map(int, desired_date.split('-'))
    # while True:
    #     next_month_button = driver.find_element(By.XPATH, "//button[@class='next-month']")
    #     displayed_date = driver.find_element(By.XPATH, "//span[@class='displayed-date']").text
    #     displayed_year, displayed_month = map(int, displayed_date.split('-'))
    #     if displayed_year == year and displayed_month == month:
    #         date_element = driver.find_element(By.XPATH, f"//div[text()='{day}']")
    #         date_element.click()
    #         break
    # next_month_button.click()
    # date_picker_button_locator ='Element'
    # date_picker_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((date_picker_button_locator)))
    # date_picker_button.click()
    # current_date = datetime.now().day
    # current_date_xpath = f"//td[contains(@class, 'today') and text()='{current_date}']"
    #
    # current_date_element = driver.find_element(by=By.XPATH, value="//td[contains(@mat-form-field-infix ng-tns-c84-29, 'today') and text()='current_date']")
    # current_date_element.click()
    # Datepicker= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='createdOnDateTime']")
    # Datepicker.click()
    # time.sleep(1)
    Date = driver.find_element(by=By.XPATH, value="//td[@aria-label='December 1, 2023']//div[@aria-selected='false']")
    Date.click()
    time.sleep(1)
    Pickerone = driver.find_element(by=By.XPATH,
                                    value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[3]/div[8]")
    Pickerone.click()
    time.sleep(1)
    Pickertwo = driver.find_element(by=By.XPATH,
                                    value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[4]/div[11]")
    Pickertwo.click()
    time.sleep(2)
    ADD_button = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    ADD_button.click()

    try:
        complete = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/app-root[1]/app-main[1]/app-pm-service-request-detail[1]/div[1]/div[1]/div[2]/ul[2]/li[1]/a[1]/span[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:
        # Error handling if success message doesn't appear within the specified time
        print("Form submission failed:", e)

    time.sleep(10)
    driver.maximize_window()
    Back = driver.find_element(by=By.XPATH, value="//a[@class='btn-backlist']//i[@class='material-icons']")
    Back.click()
    time.sleep(10)



    Inprogresslist = driver.find_element(by=By.XPATH,
                                         value="//body/app-root/app-main/app-pm-service-request-list/div/div/div/div[2]/span[1]")
    Inprogresslist.click()
    time.sleep(10)
    Srtititle = driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[1]/a[1]/span[1]/span[1]/span[2]")
    Srtititle.click()
    time.sleep(10)