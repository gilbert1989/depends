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
getXzById = ExcelUtil('isCommonCity.xlsx','getXzById')
getXzsByCountyId = ExcelUtil('isCommonCity.xlsx','getXzsByCountyId')
@ddt
class XZ(unittest.TestCase):
    def setUp(self):
        self.url = 'http://10.10.32.105/v1/'

    @data(*getXzById.next())
    def test_getXzById(self,data):
        u'''获取乡镇信息接口'''
        r =requests.get('http://10.10.32.105/v1/xz/getXzById?xzId='+str(data[0]))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        r_data = json.loads(r.text)
        db_data =db.fetchall("SELECT * FROM m_xz where id = "+str(data[0]))

        self.assertEqual(r_data['id'],str(db_data[0]['id']))
        self.assertEqual(str(r_data['countyId']),str(db_data[0]['county_id']))
        self.assertEqual(r_data['name'],db_data[0]['name'])

    @data(*getXzsByCountyId.next())
    def test_getXzsByCountyId(self,data):
        u'''根据三级区县Id查询四级乡镇'''
        r =requests.get('http://10.10.32.105/v1/xz/getXzsByCountyId/'+str(data[0]))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        r_data = json.loads(r.text)
        db_data =db.fetchall("SELECT * FROM m_xz where county_id = "+str(data[0]))
        num = len(json.loads(r.text))

        for x in range(0,num):
            self.assertEqual(r_data[x]['id'],str(db_data[x]['id']))
            self.assertEqual(r_data[x]['name'],db_data[x]['name'])
            self.assertEqual(r_data[x]['countyId'],db_data[x]['county_id'])
