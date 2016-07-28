#coding:utf-8
from selenium import webdriver
import unittest,time,json
from selenium.webdriver.common.action_chains import ActionChains
from _hashlib import new
import requests  
class jiaju(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.jyall.com"
    
    def tearDown(self):
        self.driver.quit()

    def test_newhouse_unlogin(self):
        u'''firefox未登陆状态预约新房'''
        driver = self.driver
        driver.get(self.base_url)
        #u"定位家居"
        tar = driver.find_element_by_xpath("//ul[@id='example-one']/li[2]/a") 
        ActionChains(driver).move_to_element(tar).perform()
        #u"新房"
        driver.find_element_by_xpath("//ul[@id='example-one']/li[2]/div/dl/dd/a").click()
        #u"获取当前窗口句柄"
        cur_window = driver.current_window_handle
        time.sleep(2)
       # driver.find_element_by_id('53').click()
       #u"定位新房列表第一个房源"
        driver.find_element_by_xpath("//div[@id='searchRet_List']/div/div/dl/dd/div/a").click()
        all_window = driver.window_handles
        for x in all_window:
            if x!=cur_window:
                driver.switch_to_window(x)
        time.sleep(2)
       
        driver.find_element_by_css_selector("#new_house_details_content>dd.but>button").click()
        time.sleep(1)
        driver.find_element_by_id("name").send_keys('123')
        driver.find_element_by_id("tel").send_keys('13813333333')
        #u"取验证码"
        r = requests.post("http://jiaju.jyall.com/mobiles/send-vcode?tel=13813333333&type=new")
        vcode = json.loads(r.text)["vcode"]
        driver.find_element_by_id("inputCode").send_keys(vcode)
        driver.find_element_by_id("applyValid").click()
        #u"验证alert"
        alert = driver.switch_to_alert()
        result = alert.text
        self.assertEqual(u"申请成功！", result,u'实际结果为'+result)
        
    def test_sechouse_unlogin(self):
        u'''firefox未登陆状态预约二手房'''
        driver = self.driver
        driver.get(self.base_url)
        #u"定位家居"
        tar = driver.find_element_by_xpath("//ul[@id='example-one']/li[2]/a") 
        ActionChains(driver).move_to_element(tar).perform()
        #u"二手房下拉"
        driver.find_element_by_xpath("//ul[@id='example-one']/li[2]/div/dl/dd[2]/a").click()
        #u"获取当前窗口句柄"
        cur_window = driver.current_window_handle
        time.sleep(2)
       # driver.find_element_by_id('53').click()
       #u"定位新房列表第一个房源"
        driver.find_element_by_css_selector("#searchResult>div.ju-list>div.lisetl>dl>dd>a").click()
        all_window = driver.window_handles
        for x in all_window:
            if x!=cur_window:
                driver.switch_to_window(x)
        time.sleep(2)
        #u"定位二手房"
        driver.find_element_by_css_selector("#template-secondary>dd.but>button").click()
        time.sleep(1)
        driver.find_element_by_id("name").send_keys('123')
        driver.find_element_by_id("tel").send_keys('13813333333')
        #u"取验证码"
        r = requests.post("http://jiaju.jyall.com/mobiles/send-vcode?tel=13813333333&type=used")
        vcode = json.loads(r.text)["vcode"]
        driver.find_element_by_id("inputCode").send_keys(vcode)
        driver.find_element_by_id("applyValid").click()
        #u"验证alert"
        alert = driver.switch_to_alert()
        result = alert.text
        self.assertEqual(u"申请成功！", result,u'实际结果为'+result)
    
    def test_zufang_unlogin(self):
        u'''firefox未登陆状态预约租房'''
        driver = self.driver
        driver.get(self.base_url)
        #u"定位家居"
        tar = driver.find_element_by_xpath("//ul[@id='example-one']/li[2]/a") 
        ActionChains(driver).move_to_element(tar).perform()
        #u"二手房下拉"
        driver.find_element_by_xpath("//ul[@id='example-one']/li[2]/div/dl/dd[3]/a").click()
        #u"获取当前窗口句柄"
        cur_window = driver.current_window_handle
        time.sleep(2)
       # driver.find_element_by_id('53').click()
       #u"定位新房列表第一个房源"
        driver.find_element_by_css_selector("#searchRet>div.ju-list>div.lisetl>dl>dd>div>a").click()
        all_window = driver.window_handles
        for x in all_window:
            if x!=cur_window:
                driver.switch_to_window(x)
        time.sleep(2)
        #u"定位二手房"
        driver.find_element_by_css_selector("#building>dd.but>button").click()
        time.sleep(1)
        driver.find_element_by_id("name").send_keys('123')
        driver.find_element_by_id("tel").send_keys('13813333333')
        #u"取验证码"
        r = requests.post("http://jiaju.jyall.com/mobiles/send-vcode?tel=13813333333&type=used")
        vcode = json.loads(r.text)["vcode"]
        driver.find_element_by_id("inputCode").send_keys(vcode)
        driver.find_element_by_id("applyValid").click()
        #u"验证alert"
        alert = driver.switch_to_alert()
        result = alert.text
        self.assertEqual(u"申请成功！", result,u'实际结果为'+result)
        time.sleep(3)
def temp2():
    suite = unittest.TestSuite()
    suite.addTest(jiaju("test_sechouse_unlogin"))
    return suite
if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    #report
    runner.run(temp2())
  