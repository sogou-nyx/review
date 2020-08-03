import json
import os
from selenium import webdriver
import time
import warnings
from selenium.webdriver.common.by import By
import pickle

warnings.filterwarnings('ignore')
executable_path='/Users/apple/Downloads/chromedriver'
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--proxy-server=http://swarm03.websac.hb.ted:27011')
driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options,keep_alive=False)

def get_html(query):
    driver.get(query)
    html = driver.page_source
    print(html)
    driver.close()

get_html('http://m.baidu.com/s?word=%E7%97%9B%E9%A3%8E')
