from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

user = ['_.manjeet_singh._', 'jas246leenkour', 'disha_pandita8']
message_ = ("Hello my friend how are you")


class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.user = user
        self.message = message
        self.password = password
        self.base_url = "https://www.instagram.com/"
        self.bot = driver
        self.login()

    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
        # ------- This was for my Login Page---------

        # --------- notification-----------
        # first pop up
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)

        # second pop up
        self.bot.find_element_by_xpath(
            "/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        time.sleep(2)

        # message Button
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]').click()
        time.sleep(3)

        # pressing the pencil icon
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2)
        for i in user:

            # enter the username
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(2)

            # click on the username
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div').click()
            time.sleep(2)
            # next button
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(2)

            # text area
            send = self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            # now we have to type the message
            send.send_keys(self.message)
            time.sleep(1)

            # now we have to send the message
            send.send_keys(Keys.RETURN)
            time.sleep(1)

            # opeing again the pencil to write message to other person
            self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)


def init():
    bot('arj_nitin_', 'kartik.pandita', user, message_)
    input("Done")


init()
