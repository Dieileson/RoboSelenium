from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import password

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("https://streamelements.com/velloso-1458/store")
driver.find_elements_by_xpath('/html/body/div[1]/div/md-content/navbar/md-toolbar/div/div[2]/nav[3]/button')[0].click() #login
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[1]/div/div[2]/input').send_keys(password.user) #user
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[2]/div/div[1]/div[2]/div[1]/input').send_keys(password.key) #pass
driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button')[0].click() #enter
time.sleep(60)
print ('time')
driver.back() 
driver.back()

def pay(n):
    while n == 1:
        try:
            driver.find_elements_by_xpath('/html/body/div[1]/div/md-content/div[1]/div[2]/div[3]/md-card[20]/div[2]/button')[0].click() #click 5550
            print(driver.find_elements_by_xpath('/html/body/div[4]/md-dialog/form/md-dialog-actions/div/button')[0].text, 
                driver.find_elements_by_xpath('//*[@id="app"]/div/md-content/div[1]/div[1]/div[4]/div[1]/p[1]/span/strong')[0].text) #print button and vellso point
            driver.find_elements_by_xpath('/html/body/div[4]/md-dialog/form/md-dialog-actions/div/button')[0].click() 
            driver.refresh()
            time.sleep(1.5)
        except:
            driver.refresh()
            time.sleep(1.5)
            print('pay fail')
            pay(1)
pay(1)