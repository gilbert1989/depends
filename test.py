#coding:utf-8
import json,os,time
from urllib.parse import urlencode
import requests
import unittest
import HTMLTestRunner
from ddt import data,unpack,ddt
import sys
import dbclass

if __name__ == '__main__':
    str = "123456"
    jdata = json.dumps(str)
    print(str)
    print(jdata)