from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Github:
    def __init__(self, username, password) -> None:
        self.browser = webdriver.Edge()
        self.username = username
        self.password = password
    
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(1)
        username = self.browser.find_element_by_xpath("//*[@id='login_field']")
        password = self.browser.find_element_by_id("password")
        username.send_keys(self.username)
        time.sleep(1)
        password.send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]")
        password.send_keys(Keys.ENTER)
    
    def ListFollowers(self):
        profile = self.browser.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary")
        profile.send_keys(Keys.ENTER)
        time.sleep(1)
        button = self.browser.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/a[1]")
        button.send_keys(Keys.ENTER)

    def loadFollowers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for x in items:
            a = x.find_element_by_class_name("Link--secondary")
            print(a.text)               

    def getFollowers(self):
        self.browser.get("https://github.com/sadikturan?tab=followers")
        time.sleep(1)
        self.loadFollowers()
        
        while True:
            links = self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")
            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()
                    else:
                        continue

github = Github(username, password)
github.signIn()
github.ListFollowers()
github.getFollowers()
