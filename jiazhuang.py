#coding:utf-8
from selenium import webdriver
import unittest,time,json
from selenium.webdriver.common.action_chains import ActionChains
from _hashlib import new
import requests
from nt import getcwd
import os
def login(self):
    driver = self.driver
    driver.find_element_by_link_text(u"请登录").click()
    login_button = driver.find_element_by_name("")
    driver.find_element_by_name("loginName").send_keys("13077653014")
    driver.find_element_by_name("password").send_keys('222222')
    login_button.click()
    
class jiazhuang(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.jyall.com"
    
    def tearDown(self):
        self.driver.quit()
        pass
    def test_jiazhuang_unlogin(self):
        u'''未登陆状态预约家装'''
        driver = self.driver
        driver.get(self.base_url)
        #u"定位家装"
        try:
            cur_window = driver.current_window_handle
            driver.find_element_by_xpath("//ul[@id='example-one']/li[3]/a").click()
    
            
            time.sleep(2)
            #"定位立即预约"
            all_window = driver.window_handles
            for x in all_window:
                if x!=cur_window:
                    driver.switch_to_window(x)
            cur_window = driver.current_window_handle
            driver.find_element_by_css_selector("div.bannerWarp>div.w1200>a").click()
            
            all_window = driver.window_handles
            for x in all_window:
                if x!=cur_window:
                    driver.switch_to_window(x)
            time.sleep(2)
            #u"点击我要预约"
            driver.find_element_by_css_selector("div.footer_fixed>a").click()
            time.sleep(3)
            #u"填写表单"
            driver.find_element_by_id("pro_p").click()
            driver.find_element_by_css_selector("#scroll_bd1>ul>li").click()
            
            driver.find_element_by_id("pro_t").click()
            driver.find_element_by_css_selector("#scroll_bd2>ul>li").click()
            
            driver.find_element_by_id("pro_c").click()
            driver.find_element_by_css_selector("#scroll_bd3>ul>li").click()
            
            driver.find_element_by_id("qv_address").send_keys(u"自动化测试小区地址")
            driver.find_element_by_id("address").send_keys(u"自动化测试小区楼栋门牌号")
            time.sleep(3)
    
            driver.find_element_by_name("name").send_keys("bxm")
            driver.find_element_by_id("phoneNum").send_keys("13077653014")
            
            
            #u"取验证码"
            r = requests.post("http://www.jyall.com/identifying_code.htm?mobile=13077653014")
            vcode = r.text
            driver.find_element_by_id("identity").send_keys(vcode)
            driver.find_element_by_id("remark").send_keys(u"随便吧")
            driver.find_element_by_id("yuding").click()
            driver.implicitly_wait(10)
            res = driver.find_element_by_css_selector("div.content>div.center>p").text

            self.assertEqual(res,u"预约成功",u"应提示'预约成功'，实际结果:"+res)
            #u"验证alert"
            print('123')
            #self.assertEqual(u"申请成功！", result,u'实际结果为'+result)
        except:
            driver.get_screenshot_as_file(os.getcwd()+"/photo/error.png")
        finally:
            self.assertEqual(res,u"预约成功",u"应提示'预约成功'，实际结果:"+res)
def temp2():
    suite = unittest.TestSuite()
    suite.addTest(jiazhuang("test_jiazhuang_unlogin"))
    return suite
if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    #report
    runner.run(temp2())