from byerecaptcha import solveRecaptcha
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

# # options = Options()

# # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
# # options.add_argument("--headless")
# # options.add_argument("--window-size=1920,1080")

# # options.add_argument(f'--user-agent={test_ua}')

# # options.add_argument('--no-sandbox')
# # options.add_argument("--disable-extensions")

# # test_driver = webdriver.Chrome(options=options)

# # solver = RecaptchaSolver(driver=test_driver)

# # test_driver.get('https://www.google.com/recaptcha/api2/demo')

# # recaptcha_iframe = test_driver.find_element(
# #     By.XPATH, '//iframe[@title="reCAPTCHA"]')

# # solver.click_recaptcha_v2(iframe=recaptcha_iframe)


def start_bot(**kwargs):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--no-sandbox')
    # options.add_argument("--disable-extensions")
    # options.add_argument(f'--user-agent={test_ua}')

    drive = webdriver.Chrome(options=options)
    drive.get(kwargs.get('url'))
    drive.find_element(By.ID, "login-student-tab").click()
    drive.find_element(By.ID, "confirmmodal").click()
    drive.find_element(By.ID, "email").send_keys(kwargs.get('username'))
    drive.find_element(By.ID, "password").send_keys(kwargs.get('password'))
    solveRecaptcha(drive)

    
    drive.find_element(By.ID, "login").submit()



url = "https://internship.aicte-india.org/login_new.php"
username = "chinmaypisal45@gmail.com"
password = "chinmay123"
start_bot(username=username, password=password, url=url)


# from selenium import webdriver



# options = webdriver.ChromeOptions()
# options.add_argument('--lang=en-US') #need for recaptcha be in english

# driver = webdriver.Chrome( chrome_options=options)
# driver.get('https://www.google.com/recaptcha/api2/demo')
# solveRecaptcha(driver) #FOR PREDICTION ON YOUR PC

# solveRecaptcha(driver, server="https://myserver.com") #FOR PREDICTION IN YOUR SERVER (check server.py)

# solveRecaptcha(driver, invisible=True) #FOR PREDICTION INVISIBLE CAPTCHA