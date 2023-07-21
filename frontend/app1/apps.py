# app1/apps.py
from django.apps import AppConfig
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None

class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
    
    def ready(self):
        global driver
        if driver is None:
            print("[status] : Driver Intializing ..... ")
            try:
                chrome_options = Options()
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.executable_path = 'frontend/app1/chromedriver.exe'
                driver = webdriver.Chrome(options=chrome_options)
            except Exception as e:
                print(e)
                
            print("[status] : Driver initialised.")