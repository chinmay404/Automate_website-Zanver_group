from django.shortcuts import render
from django.http import HttpResponse
from app1.apps import driver
from selenium.webdriver.common.by import By

def get_page(url):
    print(f"[status] : Driver Getting {url}")
    driver.get(url)
    h1_element = driver.find_element(By.CSS_SELECTOR, 'h1.fs-3xl')
    text = h1_element.text
    return text

def homepage(request):
    try:
        response = get_page('https://dev.to/mdrhmn/web-scraping-using-django-and-selenium-3ecg')
        if response is not None:
            return HttpResponse(f"Driver State : Working {response}")
        else :
            return HttpResponse(f"Driver State : NOT ABLE TO FETCH PAGE {response}")
    except Exception as e:
        return HttpResponse("Driver Error: " + str(e))

def shutdown(request):
    # No need to close the driver here as it will be handled by the MyAppConfig class
    return HttpResponse("Server shutdown")
