from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

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