

# ALSO TEST FILE IGNORE

from selenium import webdriver
import pickle ,urllib
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

url = "https://einvoice1.gst.gov.in/"

file_path = '/home/sirius/All/zanver project/Automate_website-Zanver_group/data/E-INVOICE_V1_JSON - 2023-07-19T142401.713(2).json'


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.set_window_size(1200, 800)

def load_cookies_from_file(file_path):
    with open(file_path, 'rb') as file:
        cookies = pickle.load(file)
    return cookies

def set_cookies_in_driver(driver, cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)

cookies = load_cookies_from_file('cookies.pkl')
driver.get(url)
driver.delete_all_cookies()
wait = WebDriverWait(driver, 10)

set_cookies_in_driver(driver, cookies)
print("Cookies added")

driver.get('https://einvoice1.gst.gov.in/UserAccount/TechPersonContacts')


btn_exit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-danger')))
btn_exit.click()
# bulk_upload_link = driver.find_element_by_link_text("Bulk Upload")
# bulk_upload_link.click()  a.btn.btn-link.parentmenu
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn.btn-link.parentmenu')))
element.click()
btn_bulk_upload = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/Invoice/BulkUpload"]')))
btn_bulk_upload.click()

try:
    file_input = driver.find_element(By.ID, 'JsonFile')
    fp = 'data/E-INVOICE_V1_JSON - 2023-07-19T142401.713(2).json'
    file_input.send_keys(file_path)
except Exception as e:
    print("File Upload Error")
    print(e)

upload_button = driver.find_element(By.ID, "uploadBtn")
upload_button.click()
print("Upload Complete.")


try:
    excel_download_link = driver.find_element(By.CSS_SELECTOR,"a.float-right.btn.btn-outline-danger.btn-sm.mr-1.btnnoloading")
    file_url = excel_download_link.get_attribute('href')  
    urllib.request.urlretrieve(file_url, "/home/sirius/All/zanver project/Automate_website-Zanver_group/excel data/response_excel_file.xlsx")
    print("Download Excel File Complete ")
except Exception as e :
    print("Eroor In Doenlading: "+e)
