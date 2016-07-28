#coding:utf-8
from selenium import webdriver
import unittest,time,json
from selenium.webdriver.common.action_chains import ActionChains
from _hashlib import new
import requests
import depend
class fitment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.jyall.com"
    def tearDown(self):
        self.driver.quit()
        pass
    def test_fitment_login(self):
        u'''登陆状态家具下订单'''
        driver = self.driver
        driver.get(self.base_url)
        depend.login(self)
        #u"定位家电"
        cur_win = driver.current_window_handle
        driver.find_element_by_css_selector("#example-one>li:nth-child(5)>a").click()
        #u"定位特定商品"
        all_window = driver.window_handles
        for x in all_window:
            if x!=cur_win:
                driver.switch_to_window(x)
        time.sleep(2)
        cur_win2 = driver.current_window_handle
        driver.find_element_by_css_selector("div.dian-right>ul>li>a>img").click()
        
        depend.switch_window(driver, cur_win2)
        driver.implicitly_wait(10)
        #u"定位购买"
        driver.find_element_by_id("buy_g").click()
        driver.implicitly_wait(10)
        #u"定位checkbox"
        driver.find_element_by_css_selector("#cart_form>div>table.shopping_table>tbody>tr:nth-child(2)>td>span.shopping_table_check1>input").click()
        #u"定位去结算"
        driver.find_element_by_css_selector("a.go_price").click()
        #u"定位提交订单"
        driver.find_element_by_id("order_save").click()
        driver.implicitly_wait(5)
        res = driver.find_element_by_css_selector("li.shopping_payfor_title").text
        self.assertEqual(res, u"订单提交成功")
        
def temp2():
    suite = unittest.TestSuite()
    suite.addTest(fitment("test_fitment_login"))
    return suite
if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    #report
    runner.run(temp2())
