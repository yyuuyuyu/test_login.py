from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
#driver.get('https://www.baidu.com/')
driver.get('http://192.168.1.185/')