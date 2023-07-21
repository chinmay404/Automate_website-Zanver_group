from django.shortcuts import render
from django.http import HttpResponse
from app1.apps import driver
from selenium.webdriver.common.by import By

def get_page(url):
    print(f"[status] :  Getting "+{url})
    driver.get(url)
    print("[status] : Succesfully Retrived Page")
    h1_element = driver.find_element(By.CSS_SELECTOR, 'h1.fs-3xl')
    text = h1_element.text
    return text

def homepage(request):
    try:
        response = get_page('https://dev.to/mdrhmn/web-scraping-using-django-and-selenium-3ecg')
        if response is not None:
            return HttpResponse(f"<center>Driver State : Working {response}</center>")
        else :
            return HttpResponse(f"<center>Driver State : NOT ABLE TO FETCH PAGE {response}</center>")
    except Exception as e:
        return HttpResponse("<center>Driver Error : " + str(e)+"</center>")

def shutdown(request):
    # No need to close the driver here as it will be handled by the MyAppConfig class
    return HttpResponse("Server shutdown")
