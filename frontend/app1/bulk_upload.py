from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.apps import driver
import pickle
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


wait = WebDriverWait(driver, 5)

def upload(files):
    
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


    # Navigate to bulk upload
    try:
        element = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.btn.btn-link.parentmenu')))
        element.click()
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
        for file in files:
            file_input.send_keys(file)

            upload_button = driver.find_element(By.ID, "uploadBtn")
            upload_button.click()

            print(f"Uploaded file: {file}")
    except Exception as e:
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
