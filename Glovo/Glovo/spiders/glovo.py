from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import scrapy
from proxy import *
import time 

class GlovoSpider(scrapy.Spider):
    name = "glovo"
    array = []
    def start_requests(self):
        driver = webdriver.Chrome()
        driver.get("https://glovoapp.com/es/es/barcelona/")
        time.sleep(3)
        url_mac = driver.find_elements(By.CSS_SELECTOR, '.store-card__link')

        for url in url_mac:
            link = url.get_attribute('href')
            print("€€€€€€€€€€")
            self.array.append(link)
            for urlt in self.array:
                print(urlt)
            print("###########")
        driver.close() 
        
    # def parse(self, response):
    #     h1 = response.meta['titulo']
    #     print("#######")
    #     print(h1)
    #     print("#######")