from app1.apps import driver
import pickle
import urllib
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def upload(files):
    wait = WebDriverWait(driver, 10)
    btn_exit = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.btn-danger')))
    btn_exit.click()

    element = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a.btn.btn-link.parentmenu')))
    element.click()
    btn_bulk_upload = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[href="/Invoice/BulkUpload"]')))
    btn_bulk_upload.click()

    try:
        file_input = driver.find_element(By.ID, 'JsonFile')
        for file_path in files:
            file_input.send_keys(file_path)

            upload_button = driver.find_element(By.ID, "uploadBtn")
            upload_button.click()

            print(f"Uploaded file: {file_path}")
    except Exception as e:
        print("File Upload Error")
        print(e)
        return False

    print("All Files Uploaded.")
    return True
