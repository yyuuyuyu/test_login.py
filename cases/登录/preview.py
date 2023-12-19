from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
#driver.get('https://www.baidu.com/')
driver.get('http://192.168.1.185/')

driver.implicitly_wait(5)
sleep(1)
#driver.find_element(By.XPATH, '//body//button[2]').click()