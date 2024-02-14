from selenium import webdriver
from selenium.common import NoSuchElementException

#global time
#import time
import pytest



from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def test_setup():
    global driver
    global time
    from pynput.keyboard import Key, Controller
    from selenium.webdriver.support import wait
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    import time
    from selenium.common import NoSuchElementException
    from selenium.webdriver import ActionChains
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    global By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
def test_pvscannegative(test_setup):
    driver.get("https://www.devpropvivo.com")
    time.sleep(10)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
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

        print("Form submission failed:", e)


    try:
        error_message = driver.find_element(By.ID, 'error_message')
        print("Error occurred:", error_message.text)
    except NoSuchElementException:
        print("No errors detected. Form submitted successfully!")
    driver.maximize_window()

    time.sleep(3)






    target_element = driver.find_element(by=By.XPATH,
                                         value="//a[@href='/association/accounts/budget']//span")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_element)
    adminutility = driver.find_element(by=By.XPATH, value="//div[14]//div[1]//h5[1]//button[1]//span[1]")
    adminutility.click()
    target_elementone = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Bounce Mail']")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementone)
    time.sleep(1)
    pvscan = driver.find_element(by=By.XPATH, value="//a[normalize-space()='PV Scan']")
    pvscan.click()
    time.sleep(4)
    linktext= driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]")
    linktext.click()
    time.sleep(4)
    driver.find_element(by=By.XPATH, value="//mat-dialog-container[@role='dialog']")
    time.sleep(2)
    crossbutton=driver.find_element(by=By.XPATH, value="//mat-dialog-container[@role='dialog']//app-email-content-dialog//div//div//span//i")
    crossbutton.click()
    time.sleep(2)
    target_elementt = driver.find_element(by=By.XPATH, value="//body//app-root//th[6]")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementt)
    time.sleep(2)
    editbutton= driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/span[2]/a[1]/i[1]")
    editbutton.click()
    time.sleep(3)
    driver.find_element(by=By.XPATH,value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pv-scan[1]/div[1]/app-pv-scan-list[1]/app-common-ax-integration-sidebar[1]/div[1]/div[2]")
    time.sleep(2)
    crossbutton=driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pv-scan/div/app-pv-scan-list/app-common-ax-integration-sidebar/div/div[@id='pv-create-sidebar']/app-upload-document/div/span/i[1]")
    crossbutton.click()
    time.sleep(2)
    uploaddocument = driver.find_element(by=By.XPATH, value="//button[@mattooltip='Upload Document']//i")
    uploaddocument.click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//div[@id='pv-create-sidebar']")
    time.sleep(1)

    # selectassociation= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Association']")
    # selectassociation.click()
    # time.sleep(1)
    # options=driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/mat-option[5]/span/span")
    # options.click()
    element = driver.find_element(by=By.XPATH, value="//body//app-root//div[@id='associationId']//div//div[1]//div[1]")
    element.click()
    time.sleep(1)
    dropdown_option = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div")

    time.sleep(5)
    # print(len(associationlist))
    option_to_select = dropdown_option.find_element(By.XPATH,
                                                    '//*[contains(text(), "Cascade Crest At Lake Stevens Condominium Owners Association")]')
    option_to_select.click()
    time.sleep(2)

    time.sleep(1)
    selectvendor = driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Vendor']")
    selectvendor.send_keys("Sansa")
    time.sleep(5)
    vendorname = driver.find_element(by=By.XPATH,
                                     value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[@role='option']/span[1]")
    vendorname.click()
    time.sleep(2)

    uploadbutton = driver.find_element(by=By.XPATH,
                                       value="//body/app-root/app-main/app-pv-scan/div/app-pv-scan-list/app-common-ax-integration-sidebar/div/div/app-upload-document/div/form[@name='frmProcessDocument']/div/button[1]")
    uploadbutton.click()
    time.sleep(4)

def test_pvscanpositive(test_setup):
    driver.get("https://www.devpropvivo.com")
    time.sleep(5)
    Login_button = driver.find_element(by=By.CSS_SELECTOR, value="#propVivoLoginBtn")
    Login_button.click()
    time.sleep(2)
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
    driver.maximize_window()
    target_element = driver.find_element(by=By.XPATH,
                                         value="//a[@href='/association/accounts/budget']//span")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_element)
    adminutility =driver.find_element(by=By.XPATH, value="//div[14]//div[1]//h5[1]//button[1]//span[1]")
    adminutility.click()
    target_elementone= driver.find_element(by=By.XPATH, value="//a[normalize-space()='Bounce Mail']")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementone)
    time.sleep(1)
    pvscan=driver.find_element(by=By.XPATH, value="//a[normalize-space()='PV Scan']")
    pvscan.click()
    time.sleep(5)
    uploaddocument= driver.find_element(by=By.XPATH, value="//button[@mattooltip='Upload Document']//i")
    uploaddocument.click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//div[@id='pv-create-sidebar']")

    # selectassociation= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Association']")
    # selectassociation.click()
    # time.sleep(1)
    # options=driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/mat-option[5]/span/span")
    # options.click()
    element = driver.find_element(by=By.XPATH, value="//body//app-root//div[@id='associationId']//div//div[1]//div[1]")
    element.click()
    time.sleep(1)
    dropdown_option = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div")

    time.sleep(5)
    # print(len(associationlist))
    option_to_select = dropdown_option.find_element(By.XPATH, '//*[contains(text(), "Cascade Crest At Lake Stevens Condominium Owners Association")]')
    option_to_select.click()
    time.sleep(2)

    time.sleep(1)
    selectvendor=driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Vendor']")
    selectvendor.send_keys("Sansa")
    time.sleep(5)
    vendorname=driver.find_element(by=By.XPATH, value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[@role='option']/span[1]")
    vendorname.click()
    time.sleep(2)

    file_input = driver.find_element(by=By.XPATH,
                                     value="/html[1]/body[1]/app-root[1]/app-main[1]/app-pv-scan[1]/div[1]/app-pv-scan-list[1]/app-common-ax-integration-sidebar[1]/div[1]/div[2]/app-upload-document[1]/div[2]/form[1]/div[4]/div[1]/button[1]/span[1]")
    file_input.click()
    time.sleep(5)
    keyboard = Controller()
    keyboard.type("file:///C:/Users/PVlap/OneDrive/Documents/Pvscaninvoice.pdf")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)

    uploadbutton=driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-pv-scan/div/app-pv-scan-list/app-common-ax-integration-sidebar/div/div/app-upload-document/div/form[@name='frmProcessDocument']/div/button[1]")
    uploadbutton.click()
    time.sleep(2)
    processdocument= driver.find_element(by=By.XPATH, value="//a[normalize-space()='Process Document']")
    processdocument.click()
    time.sleep(4)
    pdfhyperlink=driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/div[1]/div[2]/a[1]")
    pdfhyperlink.click()
    time.sleep(3)
    closebutton=driver.find_element(by=By.XPATH, value="//i[normalize-space()='close']")
    closebutton.click()
    time.sleep(2)
    searchbox=driver.find_element(by=By.XPATH, value="//body//app-root//app-main//app-process-document//app-process-document-list//div//div//div//div//div//input[@placeholder='Search here...']")
    searchbox.send_keys("CCL")
    time.sleep(2)
    editprocess=driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[1]/div[1]/div[2]/a[2]/mat-icon[1]")
    editprocess.click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//div[@id='pv-create-sidebar']")
    time.sleep(2)
    Cancelbutton= driver.find_element(by=By.XPATH, value="//form[@name='frmInvoicePayment']//button[@type='button']")
    Cancelbutton.click()

    time.sleep(2)
    process_button= driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/div[1]/div[2]/a[1]/mat-icon[1]")
    process_button.click()
    time.sleep(7)
    driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-process-document/app-process-document-detail/div/div/div/div/div[1]")
    associationname= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Association']")
    associationname.click()
    time.sleep(1)
    lista= driver.find_element(by=By.XPATH, value="//mat-option[5]//span[1]//span[1]")
    lista.click()
    selectdocumentlevel=driver.find_element(by=By.XPATH, value="//mat-select[@placeholder='Select Document Level']//div//div//span")
    selectdocumentlevel.click()
    time.sleep(2)
    selectdocumentlist= driver.find_element(by=By.XPATH, value="//mat-option[1]//span[1]")
    selectdocumentlist.click()
    time.sleep(2)
    invoicedate=driver.find_element(by=By.XPATH, value="//input[@formcontrolname='InvoiceDate']")
    invoicedate.click()
    time.sleep(2)
    Invoicedate=driver.find_element(by=By.XPATH, value="//td[@aria-label='December 1, 2023']//div[1]")
    Invoicedate.click()
    time.sleep(2)
    Invoicenumber= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='InvoiceNumber']")
    Invoicenumber.send_keys("1651561")
    time.sleep(2)
    Invoiceduedate= driver.find_element(by=By.XPATH, value="//div[3]//div[1]//div[1]//mat-form-field[1]//div[1]//div[1]//div[2]//mat-datepicker-toggle[1]//button[1]//span[1]//*[name()='svg']")
    Invoiceduedate.click()
    time.sleep(2)
    Invoiceduedatepickerone= driver.find_element(by=By.XPATH, value="//td[@aria-label='December 1, 2023']//div[1]")
    Invoiceduedatepickerone.click()
    time.sleep(2)
    Pleasesearchandselectvendor= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='Vendor']")
    Pleasesearchandselectvendor.send_keys("Sansa")
    time.sleep(8)
    Vendorname=driver.find_element(by=By.XPATH, value="//span[contains(text(),'Sansa Stark')]")
    Vendorname.click()
    time.sleep(2)
    Accountnumber=driver.find_element(by=By.XPATH, value="//input[@formcontrolname='AccountNumber']")
    Accountnumber.send_keys("12234565555")
    time.sleep(2)
    Invoiceamount=driver.find_element(by=By.XPATH, value="//input[@formcontrolname='InvoiceAmount']")
    Invoiceamount.send_keys("200")
    time.sleep(2)
    GLcodedes= driver.find_element(by=By.XPATH, value="//input[@formcontrolname='GLCode']")
    GLcodedes.click()
    GLcodedeslist= driver.find_element(by=By.XPATH, value="//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[1]/span[1]")
    GLcodedeslist.click()
    time.sleep(3)
    Addbutton= driver.find_element(by=By.XPATH, value="//button[@type='submit']")
    Addbutton.click()
    time.sleep(8)
    driver.find_element(by=By.XPATH, value="//mat-dialog-container[@role='dialog']")
    Yes_button=driver.find_element(by=By.XPATH, value="//div[@dir='ltr']//button[1]")
    Yes_button.click()
    time.sleep(4)
    processscandocument= driver.find_element(by=By.XPATH, value="//a[normalize-space()='Process Scanned Document']")
    processscandocument.click()
    time.sleep(4)
    view_button= driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[1]/div[1]/div[2]/a[1]/mat-icon[1]")
    view_button.click()
    time.sleep(2)
    target_elementtwo = driver.find_element(by=By.XPATH, value="//span[normalize-space()='AXIntegration']")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementtwo)
    time.sleep(2)
    Axintegration= driver.find_element(by=By.XPATH, value="//span[normalize-space()='AXIntegration']")
    Axintegration.click()
    time.sleep(2)
    target_elementthree = driver.find_element(by=By.XPATH, value="//a[normalize-space()='AR Charges Other']")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementthree)
    time.sleep(2)
    Apinvoice= driver.find_element(by=By.XPATH, value="//a[normalize-space()='AP Invoice']")
    Apinvoice.click()
    time.sleep(5)
    Apinvoiceview= driver.find_element(by=By.XPATH, value="//tbody/tr[2]/td[9]/a[1]/i[1]")
    Apinvoiceview.click()
    time.sleep(3)
    Editbutton= driver.find_element(by=By.XPATH, value="//mat-icon[normalize-space()='edit']")
    Editbutton.click()
    time.sleep(5)
    Crossbutton= driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-ax-integration/app-ap-invoice-detail/app-ap-invoice-payment-detail/app-common-ax-integration-sidebar/div/div/app-add-edit-invoice-sidbar/div/span/i[1]")
    Crossbutton.click()
    time.sleep(3)
    Backbutton= driver.find_element(by=By.XPATH, value="//i[normalize-space()='chevron_left']")
    Backbutton.click()
    time.sleep(3)
    Jobbutton= driver.find_element(by=By.XPATH, value="//a[normalize-space()='Job']")
    Jobbutton.click()
    time.sleep(3)
    Invoices= driver.find_element(by=By.XPATH, value="//a[@role='tab'][normalize-space()='Invoices']")
    Invoices.click()
    time.sleep(3)
    Searchbox= driver.find_element(by=By.XPATH, value="//div[@role='tabpanel']//app-ap-invoice-payment-list//div//div//div//div//div//input[@placeholder='Search here...']")
    Searchbox.send_keys(543453543)
    time.sleep(3)
    Allstatus= driver.find_element(by=By.XPATH, value="//mat-select[@placeholder='Payment Status']")
    Allstatus.click()
    time.sleep(3)
    statuslist= driver.find_element(by=By.XPATH, value="//mat-option[@role='option']//span[contains(text(),'Pending Review')]")
    statuslist.click()
    time.sleep(3)
    Allpayment= driver.find_element(by=By.XPATH, value="//mat-select[@placeholder='Payment Method']")
    Allpayment.click()
    time.sleep(3)
    Paymentoption=driver.find_element(by=By.XPATH, value="//mat-option[@role='option']//span[contains(text(),'Online')]")
    Paymentoption.click()
    time.sleep(3)
    clearallone= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-ax-integration[1]/app-ap-invoice[1]/div[1]/div[2]/div[1]/div[1]/app-ap-invoice-payment-list[1]/div[1]/div[1]/div[1]/div[1]/div[6]/button[1]")
    clearallone.click()
    time.sleep(3)
    datepicker=driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-ax-integration[1]/app-ap-invoice[1]/div[1]/div[2]/div[1]/div[1]/app-ap-invoice-payment-list[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
    datepicker.click()
    time.sleep(3)
    dateone=driver.find_element(by=By.XPATH, value="//body[1]/bs-daterangepicker-container[1]/div[1]/div[1]/div[1]/div[1]/bs-days-calendar-view[1]/bs-calendar-layout[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/span[1]")
    dateone.click()
    time.sleep(3)
    datetwo=driver.find_element(by=By.XPATH, value="//body[1]/bs-daterangepicker-container[1]/div[1]/div[1]/div[1]/div[1]/bs-days-calendar-view[1]/bs-calendar-layout[1]/div[2]/table[1]/tbody[1]/tr[5]/td[7]/span[1]")
    datetwo.click()
    time.sleep(3)
    clearallbutton=driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-ax-integration[1]/app-ap-invoice[1]/div[1]/div[2]/div[1]/div[1]/app-ap-invoice-payment-list[1]/div[1]/div[1]/div[1]/div[1]/div[6]/button[1]")
    clearallbutton.click()
    time.sleep(3)

    target_elementfour= driver.find_element(by=By.XPATH, value="//th[normalize-space()='Activity']")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementfour)

    time.sleep(3)
    APpayment= driver.find_element(by=By.XPATH, value="//a[normalize-space()='AP Payment']")
    APpayment.click()
    time.sleep(3)
    Jobbutton=driver.find_element(by=By.XPATH, value="//a[normalize-space()='Job']")
    Jobbutton.click()
    time.sleep(4)
    Paymentbutton=driver.find_element(by=By.XPATH, value="//a[normalize-space()='Payment']")
    Paymentbutton.click()
    time.sleep(3)
    Searchboxone=driver.find_element(by=By.XPATH, value="//div[@role='tabpanel']//app-ap-invoice-payment-list//div//div//div//div//div//input[@placeholder='Search here...']")
    Searchboxone.send_keys(110028)
    time.sleep(2)
    clearallpayement=driver.find_element(by=By.XPATH, value="//body/app-root/app-main/app-ax-integration/app-ap-payment/div/div/div/div[@role='tabpanel']/app-ap-invoice-payment-list/div/div/div/div/div/button[1]")
    clearallpayement.click()
    time.sleep(2)
    Invoicedaterange= driver.find_element(by=By.XPATH, value="//input[@placeholder='Invoice Date Range']")
    Invoicedaterange.click()
    time.sleep(2)
    datepay=driver.find_element(by=By.XPATH, value="//body[1]/bs-daterangepicker-container[1]/div[1]/div[1]/div[1]/div[1]/bs-days-calendar-view[1]/bs-calendar-layout[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/span[1]")
    datepay.click()
    time.sleep(2)
    datepayone=driver.find_element(by=By.XPATH, value="//body[1]/bs-daterangepicker-container[1]/div[1]/div[1]/div[1]/div[1]/bs-days-calendar-view[1]/bs-calendar-layout[1]/div[2]/table[1]/tbody[1]/tr[5]/td[8]/span[1]")
    datepayone.click()
    time.sleep(2)
    allinvoicepayment=driver.find_element(by=By.XPATH, value="//mat-select[@placeholder='Payment Status']")
    allinvoicepayment.click()
    time.sleep(2)
    readyforpayment=driver.find_element(by=By.XPATH, value="//mat-option[2]//span[1]")
    readyforpayment.click()
    time.sleep(2)
    clearallpayementone=driver.find_element(by=By.XPATH, value="//div[@role='tabpanel']//app-ap-invoice-payment-list//div//div//div//div//div//button")
    clearallpayementone.click()
    time.sleep(2)
    itemsperpage=driver.find_element(by=By.XPATH, value="//body//app-root//div[@role='tabpanel']//div//div//div//div//div//div//div//div//div//div[2]")
    itemsperpage.click()
    time.sleep(2)
    icount=driver.find_element(by=By.XPATH, value="//mat-option[4]//span[1]")
    icount.click()
    time.sleep(4)
    checkbox = driver.find_element(by=By.XPATH,
                                      value="/html[1]/body[1]/app-root[1]/app-main[1]/app-ax-integration[1]/app-ap-payment[1]/div[1]/div[2]/div[1]/div[1]/app-ap-invoice-payment-list[1]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/mat-checkbox[1]/label[1]/span[1]")
    time.sleep(2)
    if not checkbox.is_selected():
        # If the checkbox is not selected, click it to select
        checkbox.click()
    time.sleep(3)

    target_elementpv = driver.find_element(by=By.XPATH, value="//tbody/tr[38]/td[2]/span[1]")
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",
                          target_elementpv)
    time.sleep(2)

    checkboxone= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/app-root[1]/app-main[1]/app-ax-integration[1]/app-ap-payment[1]/div[1]/div[2]/div[1]/div[1]/app-ap-invoice-payment-list[1]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr[44]/td[1]/mat-checkbox[1]/label[1]/span[1]")

    if not checkboxone.is_selected():
        checkboxone.click()

    time.sleep(2)
    Readytopaybutton= driver.find_element(by=By.XPATH, value="//button[normalize-space()='Ready to Pay']")
    Readytopaybutton.click()
    time.sleep(1)

    driver.find_element(by=By.XPATH, value="//div[@class='pv-payment-process-modal']")
    time.sleep(1)
    submitbutton= driver.find_element(by=By.XPATH, value="//button[normalize-space()='Submit']")
    submitbutton.click()
    time.sleep(3)