
# TEST FILE NOT IMP


import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time ,base64
from selenium.common.exceptions import TimeoutException

url = "https://einvoice1.gst.gov.in/"
username = ""
password = ""


def start_bot(**kwargs):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1200, 800)
    driver.get(kwargs.get('url'))
    wait = WebDriverWait(driver, 10)

    login_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'button#btnLogin.homepageloginbtn')))
    login_button.click()
    print("[status] : Login Button Clicked")

    username_input = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'input#txtUserName.txtUserName')))
    username_input.clear()
    username_input.send_keys(kwargs.get('username'))

    password_input = driver.find_element(
        By.CSS_SELECTOR, 'input#txt_password.txtPassWord')
    password_input.send_keys(kwargs.get('password'))
    print("Waiting For Captcha To solve.")

    print("Sleep timer start")
    captcha_image_element = wait.until(
            EC.presence_of_element_located((By.ID, 'captcha_image')))
    screenshot = captcha_image_element.screenshot_as_png
    captcha_image_base64 = base64.b64encode(screenshot).decode('utf-8')
    # time.sleep(20)
    captcha = input("Enter Captcha")
    captcha_input_element = driver.find_element(
                    By.ID, 'CaptchaCode')
    time.sleep(3)
    for w in captcha:
        captcha_input_element.send_keys(w)
    login_button = driver.find_element(
                    By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.btnlogin')
    time.sleep(1)
    login_button.click()
    # login_button = driver.find_element(
    #     By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.btnlogin')
    # login_button.click()

    cookies = driver.get_cookies()
    file_path = '/home/sirius/All/zanver project/Automate_website-Zanver_group/frontend/'

    # Use os.path.join to construct the complete file path
    file_name = 'cookies.pkl'
    file_location = os.path.join(file_path, file_name)

    with open(file_location, 'wb') as file:
        pickle.dump(cookies, file)
    # upload_files(driver, '/home/sirius/All/zanver project/Automate_website-Zanver_group/frontend/static/json_data/E-INVOICE_V1_JSON - 2023-07-19T142401.713(2).json')
    # Check the expiry time of each cookie and print it
    print("Cookie Expiry Times:")


def upload_files(driver, file_path):
    wait = WebDriverWait(driver, 10)

    # Close any alert modal if present
    try:
        close_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-dismiss="modal"]')))
        driver.execute_script("arguments[0].click();", close_button)
        print("[status] Modal closed")
    except TimeoutException:
        print("[status] No alert modal")
        pass

    try:
        btn_exit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.btn-danger')))
        btn_exit.click()
        print("[status] Exit Button clicked")
    except TimeoutException:
        print("[status] No alert modal ")
        pass

    # Wait for the modal to disappear
    try:
        wait.until(EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, '.modal.fade.exampleModal.show')))
    except TimeoutException:
        print("[status] Modal is still visible")

    # Use JavaScript click for the element
    try:
        element = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.btn.btn-link.parentmenu')))
        driver.execute_script("arguments[0].click();", element)
        print("[status] Dropdown clicked")
    except TimeoutException:
        print("[status] Failed to click on the element")
        return False

    try:
        btn_bulk_upload = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/Invoice/BulkUpload"]')))
        btn_bulk_upload.click()
        print("[status] Bulk upload clicked")
    except TimeoutException:
        print("[status] Failed to click on bulk upload button")
        return False

    try:
        file_input = driver.find_element(By.ID, 'JsonFile')
        for file in file_path:
            file_input.send_keys(file)

            upload_button = driver.find_element(By.ID, "uploadBtn")
            upload_button.click()

            print(f"Uploaded file: {file}")
    except Exception as e:
        print("File Upload Error")
        print(e)
        return False
    
    
    
    
    try:
        upload_button = wait.until(EC.element_to_be_clickable(
            (By.ID, "uploadBtn")))
        upload_button.click()
        print("[status] Upload Button Clicked")

        print(f"Uploaded file: {file_path}")

    except TimeoutException as e:
        print("File Upload Error")
        print(e)
        return False

    # Go back to home after successful upload
    try:
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/Home/MainMenu"]'))).click()
        print("[status] Back To Home")
    except TimeoutException as e:
        print("[status] Failed to go back to home")

    return True


start_bot(username=username, password=password, url=url)
