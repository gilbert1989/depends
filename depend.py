#coding:utf-8
def login(self):
    driver = self.driver
    driver.find_element_by_link_text(u"请登录").click()
    login_button = driver.find_element_by_name("")
    driver.find_element_by_name("loginName").send_keys("13077653014")
    driver.find_element_by_name("password").send_keys('111111')
    login_button.click()

def switch_window(driver,cur_win):
    all_window = driver.window_handles
    for x in all_window:
        if x!=cur_win:
            driver.switch_to_window(x)