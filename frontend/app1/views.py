from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.apps import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import base64
import pickle
from django.contrib import messages
from selenium.common.exceptions import NoSuchElementException
from django.conf import settings
from .bulk_upload import upload


global mian_url
main_url = 'https://einvoice1.gst.gov.in/'
global wait
wait = WebDriverWait(driver, 5)


def manual_login(request):
    print("[status] Request To get url")
    driver.get(main_url)
    print("[status] Got the url")

    try:
        login_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button#btnLogin.homepageloginbtn')))
        login_button.click()
        print("[status] : Login Button Clicked")
    except Exception as te:
        print(f"[status] : Timeout Exception - {te}")
        return False
    except Exception as e:
        print(f"[status] : Exception during login - {e}")
        return False
    try:
        username_input = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input#txtUserName.txtUserName')))
        username_input.clear()
        username_input.send_keys("ACCURATESALE")
    except Exception as te:
        print(f"[status] : Timeout Exception - {te}")
        return False
    except Exception as e:
        print(f"[status] : Exception during username input - {e}")
        return False
    try:
        password_input = driver.find_element(
            By.CSS_SELECTOR, 'input#txt_password.txtPassWord')
        password_input.send_keys('Accurate@1234')
    except Exception as e:
        print(f"[status] : Exception during password input - {e}")
        return False
    try:
        captcha_image_element = driver.find_element(By.ID, 'captcha_image')
        screenshot = captcha_image_element.screenshot_as_png
        captcha_image_base64 = base64.b64encode(screenshot).decode('utf-8')
    except NoSuchElementException:
        captcha_image_base64 = None
    if request.method == 'POST':
        captcha_input = request.POST.get('captcha_input')
        print(f"[status] Captcha : {captcha_input}")
        if captcha_input:
            try:
                captcha_input_element = driver.find_element(
                    By.ID, 'CaptchaCode')
                captcha_input_element.clear()
                for w in captcha_input:
                    captcha_input_element.send_keys(w)
                login_button = driver.find_element(
                    By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.btnlogin')
                login_button.click()

                # Wait for the login process to complete before proceeding
                # wait.until(EC.presence_of_element_located((By.ID, 'some_element_that_appears_after_login')))

                # At this point, the login should be successful, and you can redirect the user or perform other actions.

            except NoSuchElementException:
                pass
    return render(request, 'manual_login.html', {'captcha_image_base64': captcha_image_base64})


def auto_login(request):
    file_path = os.path.join(os.getcwd(), 'cookies.pkl')
    with open(file_path, 'rb') as file:
        cookies = pickle.load(file)
    driver.get(main_url)
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    previous_url = driver.current_url
    driver.get('https://einvoice1.gst.gov.in/UserAccount/TechPersonContacts')
    current_url = driver.current_url
    login_successful = current_url != previous_url
    try:
        login_button = driver.find_element(
            By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.btnlogin')
    except NoSuchElementException:
        login_button = None

    if login_button is None and login_successful:
        messages.success(request, 'Login successful.')
        return redirect('home')
    else:
        # Login failed, stay on the index page
        messages.error(request, 'Login failed. Try Manual Login')
        return render(request, 'index.html')


def msi_report_download(driver):
    try:
        print("[status] Clicking MSI dropdown...")
        msi_dropdown = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.btn.btn-link.parentmenu[data-toggle="collapse"][href="#collapseFour"]')))
        msi_dropdown.click()
        msi_dropdown = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/MisRpt"]')))
        msi_dropdown.click()
        print("[status] Clicking Go button...")
        go_button = wait.until(EC.element_to_be_clickable(
            (By.ID, 'btngo')))
        go_button.click()

        print("[status] Clicking Download button...")
        download_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.btn.btn-outline-info.btn-sm.btnnoloading')))
        download_button.click()

        print("[status] Download Complete")
        return True
    except NoSuchElementException as e:
        print(f"[X] Element not found: {e}")
        return False
    except Exception as e:
        print(f"[X] Error during MSI report download: {e}")
        return False


def index_page(request):
    return render(request, 'index.html')


def home_page(request):
    json_files_dir = os.path.join(settings.STATICFILES_DIRS[0], 'json_data')
    file_names = os.listdir(json_files_dir)
    files = [os.path.join(json_files_dir, file_name)
             for file_name in file_names]
    if request.method == 'POST':
        selected_files = request.POST.getlist('selected_files')
        if not selected_files:
            messages.warning(
                request, 'No files selected. Please select at least one file.')
        else:
            print(f"[status] : Selected files {selected_files}")
            upload(selected_files)
            msi_report_download(driver)

    return render(request, 'home.html', {'files': files})


def shutdown(request):
    return HttpResponse("Server shutdown")
