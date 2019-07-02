from gophish import *
import urllib3
import os
from selenium import webdriver
import time
from pathlib import Path


# Gain access to GoPhish
api_key = 'c21434defd36f0158cb2803b2947cfec1bb0dd52296d9e645c41ecbbf4bdc27c'
urllib3.disable_warnings()
api = Gophish(api_key, host='https://127.0.0.1:3333/', verify=False)


# Auto-Open Gophish
def open_web_browser():
    home = str(Path.home())
    path = r'{}\Desktop\GoPhish\Gophish Extensions\Gophish'.format(home)
    os.chdir(path)
    os.startfile(r'gophish.exe')

    # \phishingapp\Gophish


# Login to GoPhish
def open_program():
    usernameStr = 'admin'
    passwordStr = 'gophish'
    try:
        home = str(Path.home())
        path = r'{}\Desktop\GoPhish\Gophish Extensions\chromedriver.exe'.format(home)
        browser = webdriver.Chrome(executable_path=path)
        browser.get(("https://127.0.0.1:3333/"))
        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)
        username = browser.find_element_by_name('password')
        username.send_keys(passwordStr)
        nextButton = browser.find_element_by_xpath("/html/body/div[2]/form/button")
        nextButton.click()
    except:
        print("trying another version of chromedriver")
        try:
            home = str(Path.home())
            path = r'{}\Desktop\GoPhish\Gophish Extensions\chromedriver74.exe'.format(home)
            browser = webdriver.Chrome(executable_path=path)
            browser.get(("https://127.0.0.1:3333/"))
            username = browser.find_element_by_name('username')
            username.send_keys(usernameStr)
            username = browser.find_element_by_name('password')
            username.send_keys(passwordStr)
            nextButton = browser.find_element_by_xpath("/html/body/div[2]/form/button")
            nextButton.click()
        except:
            print("no current chromedriver versions available")
