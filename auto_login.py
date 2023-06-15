from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://internship.aicte-india.org/login_new.php"
username = "chinmaypisal45@gmail.com"
password = "chinmay123"


# def start_bot(**kwargs):
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach" , True)
#     driver = webdriver.Chrome(options=options)
#     uname = kwargs.get('username')
#     pswd = kwargs.get('password')
#     url = kwargs.get('url')

#     driver.get(url)

#     driver.find_element(By.ID, "username").send_keys(uname)
#     driver.find_element(By.ID, "password").send_keys(pswd)
#     driver.find_element(By.ID, "click").click()


# def start_bot(**kwargs):
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options)
#     driver.get(kwargs.get('url'))
#     driver.find_element(By.ID, "j_username").send_keys(kwargs.get('username'))
#     driver.find_element(By.ID, "password-1").send_keys(kwargs.get('password'))
#     driver.find_element(By.CLASS_NAME, "btn-primary").click()


def start_bot(**kwargs):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    drive  = webdriver.Chrome(options=options)
    drive.get(kwargs.get('url'))
    drive.find_element(By.ID , "login-student-tab").click()
    drive.find_element(By.ID , "confirmmodal").click()
    drive.find_element(By.ID , "email").send_keys(kwargs.get('username'))
    drive.find_element(By.ID , "password").send_keys(kwargs.get('password'))
    login = drive.find_element(By.ID , "login")
    print("Waiting For Cptch To solve.")
    while login.get_attribute("disabled"):
        print("captch not solved")
    login.click()

start_bot(username=username, password=password, url=url)
