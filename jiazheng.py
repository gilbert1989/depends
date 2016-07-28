#coding:utf-8
from selenium import webdriver
import unittest,time,json
from selenium.webdriver.common.action_chains import ActionChains
from _hashlib import new
import requests
import depend,os


class jiazheng(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.jyall.com"
    
    def tearDown(self):
        self.driver.quit()
        pass
        
    def test_jiazheng_unlogin(self):
        u'''未登录预约家政'''
        driver = self.driver
        #jiazheng
        driver.get(self.base_url)
        try:
            cur_window = driver.current_window_handle
            driver.find_element_by_css_selector("#example-one>li:nth-child(6)>a").click()
            #yuyue
            depend.switch_window(driver,cur_window)
            driver.implicitly_wait(10)
            cur_win = driver.current_window_handle
            driver.find_element_by_css_selector("div.clearfix_list>ul>li>em>a").click()
            #u"填写表单"
            depend.switch_window(driver, cur_win)
            driver.find_element_by_id("pro_p").click()
            driver.find_element_by_css_selector("#scroll_bd1>ul>li:nth-child(2)").click()
            
            driver.find_element_by_id("pro_t").click()
            driver.find_element_by_css_selector("#scroll_bd2>ul>li:nth-child(1)").click()
            
            driver.find_element_by_id("pro_c").click()
            driver.find_element_by_css_selector("#scroll_bd3>ul>li:nth-child(1)").click()
            
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
            result = driver.find_element_by_css_selector("div.center>p:nth-child(1)").text
            self.assertEqual(result,u"恭喜您，已成功预约普通保洁服务！",u"预约未成功")
        except:
            driver.get_screenshot_as_file(os.getcwd()+"/photo/jiazheng.png")
        finally:
            self.assertEqual(result,u"恭喜您，已成功预约普通保洁服务！",u"预约未成功")
def temp2():
    suite = unittest.TestSuite()
    suite.addTest(jiazheng("test_jiazheng_unlogin"))
    return suite
if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    #report
    runner.run(temp2())
    