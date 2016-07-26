__author__ = 'bai.xiaoming'
import unittest,os
import country,district,city,xz
import HTMLTestRunner
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(country.Country))
    testunit.addTest(unittest.makeSuite(district.District))
    testunit.addTest(unittest.makeSuite(xz.XZ))
    testunit.addTest(unittest.makeSuite(city.City))
    #testunit.addTest(unittest.makeSuite(settleorder.settleorder))

    filename = os.getcwd()+"\\result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'基础服务',description=u'用例执行情况：')
    #执行测试用例
    runner.run(testunit)
    fp.close()