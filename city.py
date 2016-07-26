#coding:utf-8
import json,os,time
from urllib.parse import urlencode
import requests
import unittest
import HTMLTestRunner
from ddt import data,unpack,ddt
import sys
import dbclass
from ExcelUtil import  ExcelUtil

queryCitys = ExcelUtil('isCommonCity.xlsx','queryCitys')
queryCitysById =ExcelUtil('isCommonCity.xlsx','queryCitysById')
queryCommunityByDistrict = ExcelUtil('isCommonCity.xlsx','queryCommunityByDistrict')
queryCommunityById = ExcelUtil('isCommonCity.xlsx','queryCommunityById')
@ddt
class City(unittest.TestCase):
    def setUp(self):
        self.url = 'http://10.10.32.105/v1/'

    def test_queryOpenCitys(self):
        u'''获取所有开通服务城市列表'''
        r =requests.get('http://10.10.32.105/v1/city/queryOpenCitys')
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        num =db.delete("SELECT * FROM m_city_open WHERE openstatus = '1'")
        r_num= len(json.loads(r.text))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        self.assertEqual(num,r_num,"查出城市数与数据库内不符")

    def test_queryAllCitys(self):
        u'''获取所有二级城市列表接口'''
        r =requests.get('http://10.10.32.105/v1/city/queryAllCitys')
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        num =db.delete("SELECT * FROM m_city")
        r_num= len(json.loads(r.text))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        self.assertEqual(num,r_num,"查出城市数与数据库内不符")

    @data(*queryCitys.next())
    def test_queryCitys(self,data):
        u'''通过省id找城市'''
        r = requests.get('http://10.10.32.105/v1/city/queryCitys/'+str(data[0]))
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        num = db.delete('select * from m_city where province_id = '+ str(data[0]))
        resultnum = len(json.loads(r.text))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        self.assertEqual(num,resultnum,"查出城市数与数据库内不符")


    @data(*queryCitysById.next())
    def test_queryCitysById(self,data):
        u'''通过城市id找城市'''
        r = requests.get('http://10.10.32.105/v1/city/queryCityById/'+str(data[0]))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        r_data = json.loads(r.text)
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        db_data = db.fetchall('select * from m_city where id = '+ str(data[0]))

        self.assertEqual(r_data['id'],str(db_data[0]['id']))
        self.assertEqual(r_data['name'],db_data[0]['name'])
        self.assertEqual(r_data['provinceId'],db_data[0]['province_id'])
        '''
        resultnum = len(json.loads(r.text))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        self.assertEqual(num,resultnum,"查出城市数与数据库内不符")
        '''

    def test_queryAllCommunitys(self):
        u'''获取所有小区列表接口'''
        r = requests.get("http://10.10.32.105/v1/community/queryAllCommunitys")
        r_data = len(json.loads(r.text))
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        db_data = db.delete('select * from m_community')
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        self.assertEqual(r_data,db_data,'返回小区数与库内不符')

    @data(*queryCommunityByDistrict.next())
    def test_queryCommunityByDistrict(self,data):
        u'''根据商圈Id获取小区列表接口'''
        r = requests.get("http://10.10.32.105/v1/community/queryCommunityByDistrict/"+str(0))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))

        r_data = len(json.loads(r.text))

        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        db_data = db.delete("select * from m_community where district_id ="+str(data['id']))

        self.assertEqual(r_data,db_data,'返回小区数与库内不符')

    @data(*queryCommunityById.next())
    def test_queryCommunityById(self,data):
        u'''根据id获取小区信息'''
        #未完成
        r = requests.get("http://10.10.32.105/v1/community/queryCommunityById/"+str(data[0]))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code)+' 入参id为'+str(data[0]))
        r_data = len(json.loads(r.text))

        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        db_data = db.fetchall("select * from m_community where status = 1 AND id ="+str(data[0]))

def temp2():
    suite = unittest.TestSuite()
    for x in dir(City):
        if 'test_queryOpenCitys' in x:
            suite.addTest(City(x))
    return suite

if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    runner.run(temp2())
    '''
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(jyallMarket))
    filename = os.getcwd()+"\\result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'bs-cooperate-provider-166服务测试',description=u'用例执行报告')
    runner.run(testunit)
    fp.close()'''
