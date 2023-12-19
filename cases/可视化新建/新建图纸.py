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
#登录百度
driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys("admin")
sleep(1)
driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys("admin")
#登录192.168.1.150
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[1]/div/div/div/input').clear()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[1]/div/div/div/input').send_keys("admin")

driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[2]/div/div/div/input').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[2]/div/div/div/input').send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/button[3]').click()

#新建图纸
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/section/section/aside/div/div/div[1]/div/ul/div[3]/li').click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/section/section/section/main/div/div/div[3]/div[1]/div[2]/div[1]/div/div/div/div[2]').click()
sleep(3)
driver.find_element(By.XPATH, '//div[@class="event"]//button[@class="el-button el-button--primary el-button--small"]').click()
sleep(2)
driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]').click()
sleep(2)
driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]').send_keys("test")
sleep(3)
driver.find_element(By.XPATH, '//button[@class="el-button el-button--primary"]').click()
driver.find_element(By.XPATH, '//span[text()="test"]').click()
