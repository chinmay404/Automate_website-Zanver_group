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
            print("[status] : Driver Initializing ..... ")
            try:
                chrome_options = Options()
                # chrome_options.add_argument('--headless') # Without seeing the driver
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--disable-dev-shm-usage')
                # Set window size using chrome_options
                chrome_options.add_argument('--window-size=1200,800')

                # Custom Headers
                # headers = {
                #     "User-Agent": "Your User Agent String",  # Replace with the desired User-Agent
                #     "Accept-Language": "en-US,en;q=0.5"  # Replace with the desired Accept-Language
                #     # Add more headers as needed
                # }
                # for key, value in headers.items():
                #     chrome_options.add_argument(f'--header={key}:{value}')

                chrome_options.executable_path = 'frontend/app1/chromedriver.exe'
                driver = webdriver.Chrome(options=chrome_options)
            except Exception as e:
                print(e)

            print("[status] : Driver initialized.")
        else:
            print("[status] Driver Already Running ")
