#coding:utf-8
from selenium import webdriver
import unittest,time,json
from selenium.webdriver.common.action_chains import ActionChains
from _hashlib import new
import requests
def login(self):
    driver = self.driver
    driver.find_element_by_link_text(u"请登录").click()
    login_button = driver.find_element_by_name("")
    driver.find_element_by_name("loginName").send_keys("13077653014")
    driver.find_element_by_name("password").send_keys('111111')
    login_button.click()
    
class jiaju(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.jyall.com"
    
    def tearDown(self):
        #self.driver.quit()
        pass
    
    def test_reset_password(self):
        u'''修改密码'''
        driver = self.driver
        driver.get(self.base_url)
        login(self)
        #u"定位我的家园"
        driver.find_element_by_css_selector("div.top-right>ul>li:nth-child(2)>a").click()
        time.sleep(2)
        #u"定位账户信息"
        driver.find_element_by_css_selector("#user_menu>ul>li:nth-child(2)>a").click()
        #u"定位修改密码"
        driver.find_element_by_css_selector("ul.user_title_ul>li:nth-child(2)>a").click()
        
        driver.find_element_by_id("old_password").send_keys("111111")
        driver.find_element_by_id("new_password").send_keys("111111")
        driver.find_element_by_id("old_password1").send_keys("111111")
        
        driver.find_element_by_name("button").click()
