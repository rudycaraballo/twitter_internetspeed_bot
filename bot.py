from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Bot:
    def __init__(self, ad_down, ad_up, email, password):
        self.advertised_down = ad_down
        self.advertised_up = ad_up
        self.twitter_email = email
        self.twitter_password = password
        self.driver = webdriver.Chrome('../chromedriver')
       

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_btn = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_btn.click()
        #TODO: find a way to prevent driver from closing until speedtest is finsihed
        self.driver.implicitly_wait(20)
        self.driver.quit()



