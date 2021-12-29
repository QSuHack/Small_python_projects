import os
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver=webdriver.Chrome('chromedriver', options=options)
load_dotenv()
host = os.getenv("HOSTNAME")
password = os.getenv("PASSWORD")
driver.get("http://" + host+"/html/index.html")
driver.find_element_by_id("logout_span").click()
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("pop_login").click()
sleep(3)
driver.get("http://" + host+"/html/reboot.html")
driver.find_element_by_id("span_reboot_apply_button").click()
driver.find_element_by_id("pop_confirm").click()
sleep(3)
print("Success")
