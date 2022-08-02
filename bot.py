from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        
        start_btn = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_btn.click()

        #TODO extract upload and download values 
        # up_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        # down_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")

        # print(up_speed.text)
        # print(down_speed.text)
        #TODO: find a way to prevent driver from closing until speedtest is finsihed
        # down_speed = 0
        # up_speed = 0

        #self.driver implicitly waits for 20 seconds   
        
        # self.driver.quit()



