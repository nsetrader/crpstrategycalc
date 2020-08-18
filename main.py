from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import urllib

def get_url(url):
    #driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\stockinnews\\chromedriver.exe")
    #driver.get(url)
    page_source = urllib.request.urlopen(url)
    return page_source


if __name__ == "__main__":
    content = get_url("https://www.nseindia.com/market-data/live-equity-market")
    content_html = BeautifulSoup(content, 'lxml')
    print(content_html)
    print(content_html)