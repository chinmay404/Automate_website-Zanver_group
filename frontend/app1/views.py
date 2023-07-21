from django.shortcuts import render
from django.http import HttpResponse
from app1.apps import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os


global mian_url
main_url = 'https://einvoice1.gst.gov.in/'


def get_page_source(url):
    print(f"[status] :  Getting {url}")
    driver.get(url)
    print("[status] : Succesfully Retrived Page")
    return driver.page_source


def login_site(url):
    print("[status] Request To get url")
    driver.get(url)
    print("[status] Got the url")
    wait = WebDriverWait(driver, 5)

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

    return True




def auto_login(request):
    file_path = os.path.join(os.getcwd(), 'cookies.pkl')
    with open(file_path, 'rb') as file:
        cookies = pickle.load(file)
    print("[status] Cookies loaded")
    driver.get(main_url)
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    print("[status] Cookies Added")
    x = driver.get('https://ewaybillgst.gov.in/mainmenu.aspx')
    return HttpResponse(f"<center>Login Hit {x}</center>")


def homepage(request):
    print("[status] : working directory:", os.getcwd())
    return render(request, 'index.html')



def shutdown(request):
    return HttpResponse("Server shutdown")