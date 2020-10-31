from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
#path to chrome driver
PATH ="D:\chromedriver.exe"
driver =webdriver.Chrome(PATH)
driver.get("https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en-GB&ec=65620")
#enter your email login
driver.find_element_by_xpath("//input[@name=\"identifier\"]")\
    .send_keys("your login email")
button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
button.click()
time.sleep(3)
#enter your gmail password
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')\
    .send_keys("your pass word")
button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
button.click()
time.sleep(5)
#your link to the youtube vedio
driver.get('vedio link')
i=0
time.sleep(2)
page=driver.find_element_by_tag_name('html')
page.send_keys(Keys.END)
time.sleep(20)
#spaming the comment section
while True:
    button = driver.find_element_by_xpath('//*[@id="placeholder-area"]')
    button.click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="contenteditable-root"]') \
        .send_keys(f"Binod {i}")
    time.sleep(random.randint(1, 7))
    button = driver.find_element_by_xpath('//*[@id="submit-button"]')
    button.click()
    print(f"commented {i}")
    i+=1
    time.sleep(2)




