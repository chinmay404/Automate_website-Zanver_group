from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pickle
import time

url = "https://einvoice1.gst.gov.in/"
username = "ACCURATESALE"
password = "Accurate@1234"


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
    username_input.send_keys("ACCURATESALE")

    password_input = driver.find_element(
        By.CSS_SELECTOR, 'input#txt_password.txtPassWord')
    password_input.send_keys('Accurate@1234')
    print("Waiting For Captcha To solve.")

    print("Sleep timer start")
    time.sleep(10)
    login_button = driver.find_element(
        By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.btnlogin')
    login_button.click()

    cookies = driver.get_cookies()
    with open('cookies.pkl', 'wb') as file:
        pickle.dump(cookies, file)

    # Check the expiry time of each cookie and print it
    print("Cookie Expiry Times:")
    for cookie in cookies:
        print(f"Cookie Name: {cookie['name']}")
        if 'expiry' in cookie:
            print(f"Expires: {cookie['expiry']}")
            print(f"Is Expired: {time.time() > cookie['expiry']}")
        else:
            print("Cookie does not have an explicit expiry time.")
        print("-------------------------")

start_bot(username=username, password=password, url=url)



