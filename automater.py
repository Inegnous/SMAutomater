import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import schedule
import time

class instagram:
    def __init__(self,username, password):
        self.username = username
        self.password = password

    def login(self,driver):
        driver.get('https://www.instagram.com/')
        time.sleep(6)
        linkElem = driver.find_element_by_name("username")
        linkElem.send_keys(self.username)
        linkElem2 = driver.find_element_by_name("password")
        linkElem2.send_keys(self.password)
        time.sleep(3)
        login = driver.find_element_by_css_selector("button[type='submit']")
        login.click()


insta= instagram("*******","*******")
