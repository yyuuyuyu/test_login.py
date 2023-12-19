#import time
#from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#import pytest
from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(object):
    def __init__(self):
        #启动chrome浏览器
        self.driver = webdriver.Chrome()
        #指定我们需要的页面
        self.driver.get('https://www.baidu.com')
        #最大化窗口
        self.driver.maximize_window()

    def test_user_login_ok(self):
        #username = 'admin'
        #pwd = 'admin'
        #expected = 'xxx系统'
        # 定位输入用户名，并且输入用户名
        self.driver.find_element(By.XPATH,'//input[@id="kw"]').clear()
        self.driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys(username)
        # 定位输入密码，并且输入密码
        self.driver.find_element(By.XPATH,'//*[@id="el-id-1196-3"]').clear()
        self.driver.find_element(By.XPATH,'//*[@id="el-id-1196-3"]').send_keys(pwd)
        # 定位点击登录，并且点击
        #self.driver.find_element_by_class_name('el-button').click()
        # 设置等待
        sleep(3)
        # 验证登录之后的页面title和我们想要的title一致，一致表示登录成功
        #assert self.driver.title == expected
