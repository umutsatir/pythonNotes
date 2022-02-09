from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
 
#instantiate the Chrome class web driver and pass the Chrome Driver Manager
driver = webdriver.Edge()
 
#Maximize the Chrome window to full-screen
driver.maximize_window() 
 
#go to Twitter's Homepage
driver.get("https://twitter.com/") 
 
#click on the Login button
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
 
#enter your email
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys('abc@gmail.com') 
  
# enter your password
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys('Abc123.') 
  
# click on the click button  
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span').click()