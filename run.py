#coding:utf-8
import json,os,time
from urllib.parse import urlencode
import requests
import unittest
import HTMLTestRunner
import jiazhuang,jiadian,jiazheng,fitment,jiaju

if __name__ =='__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(jiadian.jiadian))
    testunit.addTest(unittest.makeSuite(jiazheng.jiazheng))
    testunit.addTest(unittest.makeSuite(fitment.fitment))
    testunit.addTest(unittest.makeSuite(jiaju.jiaju))
    testunit.addTest(unittest.makeSuite(jiazhuang.jiazhuang))
    
    filename = os.getcwd()+"\\result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'UI',description=u'结果')
    #ִ�в������� 
    runner.run(testunit)
    fp.close()