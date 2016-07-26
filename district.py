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

queryDistrictByCounty = ExcelUtil('isCommonCity.xlsx','queryDistrictByCounty')
queryDistrictById = ExcelUtil('isCommonCity.xlsx','queryDistrictById')
queryProvinceById = ExcelUtil('isCommonCity.xlsx','queryProvinceById')

@ddt
class District(unittest.TestCase):
    def setUp(self):
        self.url = 'http://10.10.32.105/v1/'

    def test_queryCountrysByCityId(self):
        u'''获取所有商圈列表接口'''
        r =requests.get('http://10.10.32.105/v1/district/queryAllDistricts')
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        r_data = json.loads(r.text)
        db_data =db.fetchall("SELECT * FROM m_district where status = 1")

        num = len(r_data)
        for x in range(0,num):
            if 'scenterId' in r_data[x]:
                self.assertEqual(r_data[x]['id'],db_data[x]['id'],'r'+ str(r_data[x])+'db'+ str(db_data[x]))
                self.assertEqual(r_data[x]['scenterId'],str(db_data[x]['scenter_id']))
                self.assertEqual(r_data[x]['name'],db_data[x]['name'])
                #self.assertEqual(r_data[x]['alias'],db_data[x]['alias'])

    @data(*queryDistrictByCounty.next())
    def test_queryDistrictByCounty(self,data):
        u'''根据区县Id获取商圈列表接口'''
        r = requests.get('http://10.10.32.105/v1/district/queryDistrictByCounty/'+str(data[0]))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        r_data = json.loads(r.text)
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        db_data =db.fetchall("SELECT * FROM m_district where county_id = " + str(data[0]))

        num = len(r_data)
        for x in range(0,num):
            self.assertEqual(r_data[x]['alias'],db_data[x]['alias'])
            self.assertEqual(r_data[x]['nameQuanpin'],db_data[x]['name_quanpin'])
            self.assertEqual(r_data[x]['countyId'],db_data[x]['county_id'])
            self.assertEqual(r_data[x]['nameJianpin'],db_data[x]['name_jianpin'])
            self.assertEqual(r_data[x]['id'],db_data[x]['id'])
            self.assertEqual(r_data[x]['name'],db_data[x]['name'])

    @data(*queryDistrictById.next())
    def test_queryDistrictById(self,data):
         u'''根据Id获取商圈信息接口'''
         r = requests.get('http://10.10.32.105/v1/district/queryDistrictById/'+str(data[0]))
         self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
         r_data = json.loads(r.text)
         db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
         db_data =db.fetchall("SELECT * FROM m_district where id = " + str(data[0]))
         #self.assertEqual(r_data['alias'],db_data[0]['alias'])

    @data('true','false')
    def test_queryAllProvinces(self,bool):
        u'''获取所有省份信息'''
        r = requests.get('http://10.10.32.105/v1/province/queryAllProvinces?containChilds='+bool)
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        r_data = len(json.loads(r.text))

        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        db_data =db.delete("SELECT * FROM m_province")
        self.assertEqual(r_data,db_data,'查出数与库内不一致')

    @data(*queryProvinceById.next())
    def test_queryProvinceById(self,data):
        u'''获取单个省份信息'''
        r = requests.get('http://10.10.32.105/v1/province/queryProvinceById/'+str(data[0]))
        self.assertEqual(r.status_code,200,"返回值应为200，实为："+str(r.status_code))
        r_data = json.loads(r.text)
        db = dbclass.dbClass('10.10.20.108','jsjy','jsjy2015','common')
        db_data =db.fetchall("SELECT * FROM m_province where id ="+str(data[0]))
        self.assertEqual(r_data['id'],str(db_data[0]['id']))
        self.assertEqual(r_data['name'],db_data[0]['name'])
