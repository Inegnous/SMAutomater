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

def job():
    browser = webdriver.Chrome(executable_path='C:\\Games\\chromedriver.exe')
    insta.login(browser)

    time.sleep(3)
    message=browser.find_element_by_class_name("xWeGp")
    message.click()
    time.sleep(3)
    notnow=browser.find_element_by_css_selector("button[tabindex='0']")
    notnow.click() 
    dev= browser.find_element_by_xpath("//div[text()='_oneredchrysomallos_']")
    dev.click()
    time.sleep(3)
    notnow=browser.find_element_by_css_selector("button[tabindex='0']")
    notnow.click() 
    sendmessage=browser.find_element_by_css_selector("textarea[style='height: 18px;']")
    sendmessage.send_keys('I love you')
    sendmessage.send_keys(Keys.ENTER)
    
schedule.every().minute.at(":40").do(job)
schedule.every().monday.at("14:37").do(job)
schedule.every().tuesday.at("14:00").do(job)
schedule.every().wednesday.at("14:30").do(job)
schedule.every().thursday.at("13:55").do(job)
schedule.every().friday.at("13:22").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
