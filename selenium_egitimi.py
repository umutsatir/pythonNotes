from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# NOT: XML VE XPATH'DE INDEX NUMARALARI 1'DEN BAŞLAR!!!

driver = webdriver.Edge()

url = "https://github.com"

driver.get(url)
time.sleep(2)
print(driver.title)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.png")

url = "https://github.com/umutsatir"

driver.get(url)
time.sleep(2)
driver.back() # sayfayı arkaplana alma
driver.forward() # sayfayı öne alma
time.sleep(2)
driver.close()




## SELENIUM İLE SAYFA ETKİLEŞİMİ ##

driver = webdriver.Edge()
url = "https://github.com"
driver.get(url)
time.sleep(2)
searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_elements_by_css_selector(".repo-list-item h3 a")

for element in result:
    print(element.text)



## INSTAGRAM OTOMATİK TAKİP ##

class Instagram:
    def __init__(self, email, password) -> None:
        self.browser = webdriver.Edge()
        self.email = email
        self.password = password
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/?hl=tr")
        time.sleep(2)
        emailx = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        emailx.send_keys(self.email)
        passwordx = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        passwordx.send_keys(self.password)
        passwordx.send_keys(Keys.ENTER)
        time.sleep(5)
   
    def followUser(self,username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Takiptesin":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin.")
    
    def unfollowUser(self,username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        unfollowButton = self.browser.find_element_by_tag_name("button")
        if unfollowButton.text == "Takiptesin":
            unfollowButton.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('//button[text()="Takibi Bırak"]').click()
        else:
            print("Zaten kullanıcıyı takip etmiyorsun.")


insta = Instagram("umut_satir","***********")
insta.signIn()
insta.followUser("apple")
time.sleep(2)
insta.unfollowUser("apple")
