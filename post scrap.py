from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
#from parsel import Selector
import json

mailid = []

#Make sure you added your username and password in acc.json file before executing.
acc = json.load(open("acc.json", "r"))

d = webdriver.Chrome()
wait = WebDriverWait(d, 10)
d.get("https://www.linkedin.com/")
d.maximize_window()
signin = d.find_element_by_class_name("nav__button-secondary")
signin.click()
time.sleep(2)
mailfield = d.find_element_by_id("username")
passfield = d.find_element_by_id("password")
mailfield.send_keys(acc["user"])
passfield.send_keys(acc["pass"])
passfield.send_keys("\n")

d.get('https://www.google.com/')
search_input = d.find_element_by_name('q')
search_input.send_keys('site:linkedin.com/in/ AND "python developer" AND "India"')
search_input.send_keys(Keys.RETURN)

profiles = d.find_elements_by_xpath('//*[@class="r"]/a[1]')
profiles = [profile.get_attribute('href') for profile in profiles]
print(profiles)
for profile in profiles:
    d.get(profile)
    print(profile)

    try:
        time.sleep(2)
        d.get(d.find_element_by_link_text('Contact info').get_attribute('href'))
        time.sleep(2)
        mailid.append((d.find_element_by_partial_link_text("@gmail.com").get_attribute('href'))[7:])
        print((d.find_element_by_partial_link_text("@gmail.com").get_attribute('href'))[7:])
        time.sleep(2)

    except:
        print('Email Not Found...')
