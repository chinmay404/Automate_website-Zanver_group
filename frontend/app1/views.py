# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.apps import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import base64
import pickle
import time
from django.contrib import messages
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from django.conf import settings
from .bulk_upload import upload

username = "ACCURATESALE#VIN"
password = "Einvoice@1"

main_url = 'https://einvoice1.gst.gov.in/'
wait = WebDriverWait(driver, 5)


def back_to_home():
    try:
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/Home/MainMenu"]'))).click()
    except Exception as e:
        print(f"[X] Error during back_to_home: {e}")


def logged_status():
    return driver.current_url != main_url


def change_user_info(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        new_password = request.POST.get('new_password')
        global username, password
        username = new_username
        password = new_password
        return redirect('')

    return render(request, 'user_info.html')


def manual_login(request):
    if request.method == 'POST' and 'captcha_input' in request.POST:
        # This is the manual_login page POST request
        captcha_input = request.POST['captcha_input']
        print(f"[status] Captcha : {captcha_input}")
        if captcha_input:
            try:
                captcha_input_element = driver.find_element(
                    By.ID, 'CaptchaCode')
                time.sleep(3)
                captcha_input_element.clear()  # Clear the captcha input field
                captcha_input_element.send_keys(captcha_input)

                login_button = driver.find_element(
                    By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.btnlogin')
                login_button.click()
                print('[status] Login Successful')
                cookies = driver.get_cookies()

                # Save the cookies to a cookies.pkl file in the static folder
                cookies_file_path = os.path.join(settings.STATICFILES_DIRS[0], 'cookies.pkl')
                with open(cookies_file_path, 'wb') as f:
                    pickle.dump(cookies, f)

                # At this point, the login should be successful, and you can redirect the user or perform other actions.
                return redirect('home')

            except NoSuchElementException:
                pass

    # This is the first page with Auto Login and Manual Login buttons
    print("[status] Request To get url")
    driver.get(main_url)
    print("[status] Got the url")

    try:
        # Wait for the login button to be clickable, and then click it
        login_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button#btnLogin.homepageloginbtn')))
        login_button.click()
        print("[status] : Login Button Clicked")
    except TimeoutException:
        print("[status] : Timeout waiting for the login button to be clickable")
        return False

    try:
        # Wait for the username input element to be visible, and then send keys
        username_input = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input#txtUserName.txtUserName')))
        username_input.clear()
        username_input.send_keys(username)
    except TimeoutException:
        print(
            "[status] : Timeout waiting for the username input element to be visible")
        return False

    try:
        # Wait for the password input element to be visible, and then send keys
        password_input = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input#txt_password.txtPassWord')))
        password_input.send_keys(password)
    except TimeoutException:
        print(
            "[status] : Timeout waiting for the password input element to be visible")
        return False

    try:
        # Wait for the captcha image element to be present, then take a screenshot and encode it to base64
        captcha_image_element = wait.until(
            EC.presence_of_element_located((By.ID, 'captcha_image')))
        screenshot = captcha_image_element.screenshot_as_png
        captcha_image_base64 = base64.b64encode(screenshot).decode('utf-8')
    except NoSuchElementException:
        captcha_image_base64 = None

    return render(request, 'manual_login.html', {'captcha_image_base64': captcha_image_base64})


def auto_login(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'cookies.pkl')
    print(f"[status] File Path : {file_path}")
    try:
        with open(file_path, 'rb') as file:
            cookies = pickle.load(file)
    except FileNotFoundError as e:
        print(f"[X] FileNotFoundError: {e}")
        cookies = []

    driver.get(main_url)
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)

    previous_url = driver.current_url
    driver.get('https://einvoice1.gst.gov.in/Home/MainMenu')
    current_url = driver.current_url
    login_successful = current_url != previous_url

    try:
        login_button = driver.find_element(
            By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.btnlogin')
    except NoSuchElementException:
        login_button = None

    if login_button is None and login_successful:
        messages.success(request, 'Login successful.')
        back_to_home()
        return redirect('home')
    else:
        # Login failed, stay on the index page
        print("[status] Cookies Expired 'Collect New cookies'")
        messages.error(request, 'Login failed. Try Manual Login')
        return render(request, 'index.html')


def msi_report_download():
    try:
        msi_dropdown = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.btn.btn-link.parentmenu[data-toggle="collapse"][href="#collapseFour"]')))
        msi_dropdown.click()
        print("[status] Clicked MSI dropdown...")
    except NoSuchElementException as e:
        print(f"[X] Element not found while clicking MSI dropdown: {e}")
        back_to_home()
        return False
    except TimeoutException as e:
        print(f"[X] Timeout while waiting for MSI dropdown: {e}")
        back_to_home()
        return False

    try:
        msi_dropdown = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/MisRpt"]')))
        msi_dropdown.click()
    except NoSuchElementException as e:
        print(f"[X] Element not found while clicking MSI report: {e}")
        back_to_home()
        return False
    except TimeoutException as e:
        print(f"[X] Timeout while waiting for MSI report: {e}")
        back_to_home()
        return False

    try:
        go_button = wait.until(EC.element_to_be_clickable((By.ID, 'btngo')))
        go_button.click()
    except NoSuchElementException as e:
        print(f"[X] Element not found while clicking Go button: {e}")
        back_to_home()
        return False
    except TimeoutException as e:
        print(f"[X] Timeout while waiting for Go button: {e}")
        back_to_home()
        return False

    try:
        download_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.btn.btn-outline-info.btn-sm.btnnoloading')))
        download_button.click()
        back_to_home()
        print("[status] Download Complete")
        return True
    except NoSuchElementException as e:
        print(f"[X] Element not found while clicking Download button: {e}")
        back_to_home()
        return False
    except TimeoutException as e:
        print(f"[X] Timeout while waiting for Download button: {e}")
        back_to_home()
        return False
    except Exception as e:
        print(f"[X] Error during MSI report download: {e}")
        back_to_home()
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
            upload_status = upload(selected_files)
            if upload_status == 'upload_positive':
                msi_report_download()
            elif upload_status == 'not_loggedin':
                # Add message of logged out from site
                return redirect('home')
            else:
                return HttpResponse("File Upload Error")

    return render(request, 'home.html', {'files': files})


def shutdown(request):
    return HttpResponse("Server shutdown")
