from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:\chromedriver.exe"
link = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_WT=2&geoId=102713980&keywords=python%20developer" \
       "&location=India&sortBy=R "

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(link)

sign_button = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
sign_button.click()

user_name = driver.find_element_by_id("username")
user_name.send_keys("k.balaganesh26@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("bala2003")

sign_in_button = driver.find_element_by_css_selector(".login__form_action_container button")
sign_in_button.click()

apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
apply_button.click()

phone_number = driver.find_element_by_css_selector(".display-flex input")
phone_number.send_keys("9445543026")
time.sleep(2)
next_button = driver.find_element_by_id("ember363")
next_button.click()


