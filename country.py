#coding:utf-8
import json,os,time
from urllib.parse import urlencode
import requests
import unittest
import HTMLTestRunner
from ddt import data,unpack,ddt
import sys
import dbclass
from ExcelUtil import ExcelUtil


queryCountrysByCityId = ExcelUtil('isCommonCity.xlsx','queryCitysById')
queryCountryById = ExcelUtil('isCommonCity.xlsx','queryCountryById')
@ddt
class Country(unittest.TestCase):
    def setUp(self):
        self.url = 'http://10.10.32.105/v1/'

    @data(*queryCountrysByCityId.next())
    def test_queryCountrysByCityId(self,data):
        u'''根据二级城市ID获取三级区县列表'''
        r =requests.get('http://10.10.32.105/v1/country/queryCountrysByCityId/'+str(data[0]))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        r_data = json.loads(r.text)
        db_data =db.fetchall("SELECT id,city_id,name FROM m_county where status = 1 AND city_id = "+  str(data[0]))
        num = len(r_data)
        for x in range(0,num):
            self.assertEqual(r_data[x]['id'],str(db_data[x]['id']))
            self.assertEqual(str(r_data[x]['cityId']),str(db_data[x]['city_id']))
            self.assertEqual(r_data[x]['name'],db_data[x]['name'])

    @data(*queryCountryById.next())
    def test_queryCountryById(self,data):
        u'''根据三级iD获取三级区县列表'''
        r = requests.get('http://10.10.32.105/v1/country/queryCountryById/'+str(data[0]))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        r_data = json.loads(r.text)
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        db_data =db.fetchall("SELECT * FROM m_county where id = "+  str(data[0]))

        self.assertEqual(r_data['id'],str(db_data[0]['id']))
        self.assertEqual(str(r_data['cityId']),str(db_data[0]['city_id']))
        self.assertEqual(r_data['name'],db_data[0]['name'])