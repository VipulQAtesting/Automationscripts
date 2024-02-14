from selenium import webdriver
from selenium.common import NoSuchElementException
import pytest

from pynput.keyboard import Key, Controller
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture()
def test_setupforpoll():
    global driver
    import time
    global time
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    global By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)

def test_pvscannegative(test_setupforpoll):
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

    manageassociation= driver.find_element(by=By.XPATH, value="//span[normalize-space()='Manage Association']")
    manageassociation.click()
    time.sleep(2)
    pollbutton=driver.find_element(by=By.XPATH, value="//a[normalize-space()='Poll']")
    pollbutton.click()
    time.sleep(2)

    poll_button = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Poll']")
    poll_button.click()
    time.sleep(3)
    addpoll_button= driver.find_element(by=By.XPATH, value="//button[@mattooltip='Add Poll']")
    addpoll_button.click()
    time.sleep(2)
    frame = driver.find_element(by=By.XPATH, value="/html/body/app-root/app-main/app-poll-v1/app-add-edit-poll-v1/div/div/div[2]/app-poll-form/form")
    time.sleep(2)
    Publish_buttonone =driver.find_element(by=By.CSS_SELECTOR, value="body > app-root > app-main > app-poll-v1 > app-add-edit-poll-v1 > div > div > div.add-edit-poll-v1__container > app-poll-form > form > div:nth-child(2) > div.col-md-12 > div > button:nth-child(3)")
    Publish_buttonone.click()

    time.sleep(2)


def testpollpositive(test_setupforpoll):


    driver.get("https://www.devpropvivo.com")
    time.sleep(10)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(3)

    try:
        emailfield = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/app-root[1]/app-login[1]/div[1]/div[1]/div[2]/form[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]'))
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

    manageassociation = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Manage Association']")
    manageassociation.click()
    time.sleep(2)
    target_element = driver.find_element(by=By.XPATH,
                                         value="/html[1]/body[1]/app-root[1]/app-main[1]/app-header[1]/nav[1]/div[1]/div[10]/div[1]/h5[1]/ul[1]/li[1]/a[1]")

    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_element)
    time.sleep(3)
    pollbutton = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Poll']")
    pollbutton.click()
    time.sleep(8)
    addpoll_button = driver.find_element(by=By.XPATH, value="//button[@mattooltip='Add Poll']")
    addpoll_button.click()
    time.sleep(8)
    frame = driver.find_element(by=By.XPATH,
                                value="/html/body/app-root/app-main/app-poll-v1/app-add-edit-poll-v1/div/div/div[2]/app-poll-form/form")
    time.sleep(2)
    Selectassociation_dropdown = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='AssociationId']")
    Selectassociation_dropdown.click()
    time.sleep(2)
    pleaseselectassociationlist = driver.find_element(by=By.XPATH,
                                                      value="//span[contains(text(),'Good Luck Association')]")
    pleaseselectassociationlist.click()
    time.sleep(2)
    Question = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Question']")
    Question.send_keys("Test poll for new scriptwrritting")
    time.sleep(2)
    Description = driver.find_element(by=By.XPATH, value="//div[@title='Rich Text Editor, editor1']")
    Description.send_keys("Test new poll")
    time.sleep(3)

    driver.find_element(by=By.XPATH,
                        value="//body/app-root/app-main/app-poll-v1/app-add-edit-poll-v1/div/div/div/app-poll-form/form/div/div[3]")
    time.sleep(3)
    file_input = driver.find_element(by=By.XPATH,
                                     value="/html/body/app-root/app-main/app-poll-v1/app-add-edit-poll-v1/div/div/div[2]/app-poll-form/form/div[1]/div[3]/div/div[2]/button")
    file_input.click()
    time.sleep(4)
    keyboard = Controller()

    keyboard.type("C:\\Users\\PVlap\\Downloads\\Mail.pdf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # file_input.send_keys("C://Users/PVlap/Downloads/Mail.pdf")
    # # file_path= os.path.abspath("C://Users/PVlap/Downloads/Pvscan.pdf")
    # # file_input.send_keys(file_path)
    time.sleep(3)

    Option1 = driver.find_element(by=By.XPATH,
                                  value="//div[4]//div[1]//mat-form-field[1]//div[1]//div[1]//div[1]//input[1]")
    Option1.send_keys("Yes")
    time.sleep(2)
    Option2 = driver.find_element(by=By.XPATH,
                                  value="//div[5]//div[1]//mat-form-field[1]//div[1]//div[1]//div[1]//input[1]")
    Option2.send_keys("NO")
    Datetimepicker = driver.find_element(by=By.XPATH, value="//*[name()='path' and contains(@d,'M15,13H16.')]")
    Datetimepicker.click()
    time.sleep(2)
    date = driver.find_element(by=By.XPATH, value="//div[normalize-space()='30']")
    date.click()

    timehrs = driver.find_element(by=By.XPATH,
                                  value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[3]/div[7]")
    timehrs.click()

    timemin = driver.find_element(by=By.XPATH,
                                  value="/html/body/div[5]/div[2]/div/mat-datetimepicker-content/mat-datetimepicker-calendar/div[2]/mat-datetimepicker-clock/div/div[4]/div[9]")
    timemin.click()
    time.sleep(2)
    previewbutton= driver.find_element(by=By.XPATH, value="//button[normalize-space()='Preview']")
    previewbutton.click()
    time.sleep(2)

    crossbutton=driver.find_element(by=By.XPATH, value="//mat-icon[normalize-space()='close']")
    crossbutton.click()
    time.sleep(2)
    Publish_button = driver.find_element(by=By.CSS_SELECTOR,
                                    value="body > app-root > app-main > app-poll-v1 > app-add-edit-poll-v1 > div > div > div.add-edit-poll-v1__container > app-poll-form > form > div:nth-child(2) > div.col-md-12 > div > button:nth-child(3)")
    Publish_button.click()
    time.sleep(8)
    Activebutton= driver.find_element(by=By.XPATH,value="//body/app-root/app-main/app-poll-v1/app-poll-list-v1/div/div/div/div[2]/span[1]")
    Activebutton.click()
    time.sleep(8)
    title= driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[1]/a[1]/span[1]/span[1]/span[2]")
    title.click()
    time.sleep(8)
    summary=driver.find_element(by=By.XPATH, value="//span[normalize-space()='Summary']")
    summary.click()
    time.sleep(2)
    Details=driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-poll-v1[1]/app-poll-detail-v1[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[1]")
    Details.click()
    time.sleep(4)
    pdfdownloadbutton=driver.find_element(by=By.XPATH, value="//img[@src='../../../../assets/images/icon-images/pdf.png']")
    pdfdownloadbutton.click()
    time.sleep(6)

    Backbutton= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-poll-v1[1]/app-poll-detail-v1[1]/div[1]/div[1]/div[1]/a[1]/mat-icon[1]")
    Backbutton.click()
    time.sleep(7)
    completedbutton= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-poll-v1[1]/app-poll-list-v1[1]/div[1]/div[1]/div[2]/div[3]/span[1]")
    completedbutton.click()
    time.sleep(7)
    deletedbutton= driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-poll-v1/app-poll-list-v1/div/div/div/div[4]/span[1]")
    deletedbutton.click()
    time.sleep(7)
    Allbutton= driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-poll-v1/app-poll-list-v1/div/div/div/div[5]/span[1]")
    Allbutton.click()
    time.sleep(7)
    paginationarrow=driver.find_element(by=By.XPATH, value="//button[@aria-label='Next page']//span[1]//*[name()='svg']")
    paginationarrow.click()
    time.sleep(8)

def test_pollbyBM(test_setupforpoll):
    driver.get("https://www.devpropvivo.com")
    time.sleep(10)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(3)

    try:
        emailfield = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html[1]/body[1]/app-root[1]/app-login[1]/div[1]/div[1]/div[2]/form[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)

    Email_box = driver.find_element(by=By.ID, value="mat-input-0")
    Email_box.send_keys("yash.bmtekgrid@gmail.com")
    time.sleep(1)
    Password_box = driver.find_element(by=By.ID, value="mat-input-1")
    Password_box.send_keys("Abcd123#")
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
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-dashboard/div[@id='infinite-list']/div/div/div[@id='mainfeeds']/div[@id='myfeed']/form[@name='frmComment']/div[@formarrayname='comments']/div[1]/div[1]/div[1]")

    yesfromBm= driver.find_element(by=By.XPATH, value="//div[@formarrayname='comments']//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//div[1]//button[1]")
    yesfromBm.click()
    time.sleep(2)
    checkresult =driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-dashboard/div[@id='infinite-list']/div/div/div[@id='mainfeeds']/div[@id='myfeed']/form[@name='frmComment']/div[@formarrayname='comments']/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
    checkresult.click()

    time.sleep(3)

    manageassociation = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Manage Association']")
    manageassociation.click()
    time.sleep(2)

    Addpoll_button= driver.find_element(by=By.XPATH, value="//a[normalize-space()='Poll']")
    Addpoll_button.click()
    time.sleep(6)

    polltitle= driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[1]/a[1]/span[1]")
    polltitle.click()
    time.sleep(8)


def test_pollbyHO(test_setupforpoll):
    driver.get("https://www.devpropvivo.com")
    time.sleep(10)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(3)

    try:
        emailfield = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html[1]/body[1]/app-root[1]/app-login[1]/div[1]/div[1]/div[2]/form[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]'))
        )
        print("Form submitted successfully!")
    except Exception as e:

        print("Form submission failed:", e)

    Email_box = driver.find_element(by=By.ID, value="mat-input-0")
    Email_box.send_keys("peter.roy98@yahoo.com")
    time.sleep(1)
    Password_box = driver.find_element(by=By.ID, value="mat-input-1")
    Password_box.send_keys("Abcd123#")
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
    time.sleep(3)

    Yesoptionfroho=driver.find_element(by=By.XPATH, value="//div[@formarrayname='comments']//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//div[1]//button[1]")
    Yesoptionfroho.click()