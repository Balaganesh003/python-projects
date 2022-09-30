import os
import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\chromedriver.exe"
insta_link = "https://www.instagram.com/"
email_id = "k.balaganesh26@gmail.com"
insta_password = os.environ.get("password")



class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get(insta_link)
        time.sleep(5)
        email = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        email.send_keys(email_id)

        password = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password.send_keys(insta_password)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        account_search = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        account_search.send_keys(similar_account)
        time.sleep(5)
        account_search.send_keys(Keys.ENTER)
        time.sleep(5)
        account_search.send_keys(Keys.ENTER)
        time.sleep(3)
        followers_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(10)
        fBody = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = True
        now = time.time()
        time_after = now + 60
        # while scroll:  # scroll 5 times
        #     if time.time() < time_after:
        #         self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments['
        #                                    '0].offsetHeight;', fBody)
        #     else:
        #         scroll = False

    def follow(self):
        followers = self.driver.find_elements_by_css_selector("li div button")
        for each_person in followers:
            try:
                each_person.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                time.sleep(5)
                cancel = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel.click()
                time.sleep(10)


bot = InstaFollower()
bot.login()
time.sleep(10)
bot.find_followers()
time.sleep(5)
bot.follow()
