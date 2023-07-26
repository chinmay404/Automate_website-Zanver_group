import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64


def login_to_website():
    driver = selenium.webdriver.Chrome()
    driver.get("https://einvoice1.gst.gov.in/")

    username = "ACCURATESALE#VIN"
    password = "Einvoice@1"

    login_button = driver.find_element(By.CSS_SELECTOR, "button#btnLogin.homepageloginbtn")
    login_button_clickable = EC.element_to_be_clickable(login_button)
    WebDriverWait(driver, 10).until(login_button_clickable)
    login_button.click()

    username_input = driver.find_element(By.CSS_SELECTOR, "input#txtUserName.txtUserName")
    wait_until_clickable(driver, username_input)
    username_input.send_keys(username)

    password_input = driver.find_element(By.CSS_SELECTOR, "input#txt_password.txtPassWord")
    wait_until_clickable(driver, password_input)
    password_input.send_keys(password)

    captcha_image_element = driver.find_element(By.ID, "captcha_image")
    screenshot = captcha_image_element.screenshot_as_png
    captcha_image_base64 = base64.b64encode(screenshot).decode('utf-8')

    captcha_input = input("Enter the captcha: ")

    captcha_input_feild = driver.find_element(By.ID, "CaptchaCode")
    captcha_input_feild.click()
    wait_until_clickable(driver, captcha_input_feild)
    captcha_input_element = driver.find_element(By.ID, "CaptchaCode")
    captcha_input_element.send_keys(captcha_input)

    login_button2 = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block.btnlogin")
    login_button2_clickable = EC.element_to_be_clickable(login_button2)
    WebDriverWait(driver, 10).until(login_button2_clickable)
    login_button2.click()


def wait_until_clickable(driver, element):
    element_clickable = EC.element_to_be_clickable(element)
    WebDriverWait(driver, 10).until(element_clickable)


if __name__ == "__main__":
    login_to_website()
