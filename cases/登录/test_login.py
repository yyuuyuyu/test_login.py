from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
#driver.get('https://www.baidu.com/')
driver.get('http://192.168.1.185/')

#driver.implicitly_wait(5)
#登录百度
#driver.find_element(By.XPATH, '//input[@id="kw"]').clear()
#sleep(1)
#driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys("admin")
#登录192.168.1.150
#driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[1]/div/div/div/input').clear()
#sleep(1)
#driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[1]/div/div/div/input').send_keys("admin")

#driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[2]/div/div/div/input').click()
#sleep(1)
#driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[2]/div/div/div/input').send_keys("admin")
#driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/button[3]').click()




