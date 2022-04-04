from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import time

nick = input("Please type your Instagram username: ")
pwd = input("Please type your Instagram password: ")

driver = webdriver.Chrome()

url = "https://www.instagram.com/accounts/login/"

driver.get(url)
time.sleep(10)

##### TO BE CONTINUED #####