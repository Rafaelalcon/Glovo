from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import scrapy


class GlovoSpider(scrapy.Spider):
    name = "glovo"
    
    def start_requests(self):
        driver = webdriver.Chrome()
        driver.get("https://glovoapp.com/es/es")
        titulo = driver.find_element(By.CSS_SELECTOR, 'h1.global-jumbotron__text-container__title').text
        driver.close()
        yield scrapy.Request(url="https://glovoapp.com/es/es", callback=self.parse, meta={'titulo': titulo})
        
    def parse(self, response):
        titulo = response.meta['titulo']
        print(titulo)