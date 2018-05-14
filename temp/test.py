# import unittest
#
# import paramunittest
#
# from common import common
#
# productInfo_xls = common.get_xls("productCase.xlsx", "getProductInfo")
# @paramunittest.parametrized(*productInfo_xls)
# class test(unittest.TestCase):
#     def setParameters(self, case_name, method, token, goods_id, result, code, msg):
#         self.case_name = case_name
#         print(case_name)
#         self.method = method
#         print(method)
#         self.token = token
#         self.goods = goods_id
#         self.result = result
#         self.code = code
#         self.msg = msg
#
#     @classmethod
#     def testcase(cls):
#         cls.setParameters()
        # print(cls.case_name)
        # print(cls.method)
#
# test.testcase()
# if __name__ == '__main__':
#     test = test(object)
# import time
#
# print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

import unittest

import paramunittest
import time

import readConfig
from common import configHttp, configDB, common
from common.Log import MyLog

dataPlatformUserCase_xls = common.get_xls("dataPlatformUserCase.xlsx", "UvLoadChartData")
localConfigHttp = configHttp.ConfigHttp()
localReadConfig = readConfig.ReadConfig()
# localConfigDB = configDB.MyDB()

@paramunittest.parametrized(*dataPlatformUserCase_xls)
class UvLoadChartData(unittest.TestCase):

    def setParameters(self,case_name,startTime,endTime,stats,type,name):
        self.case_name = str(case_name)
        self.startTime = str(startTime)
        self.endTime = str(endTime)
        self.stats = str(stats)
        self.type = str(type)
        self.name = str(name)

    def test(self):
        print(type(self.case_name))

if __name__ == '__main__':
    test = UvLoadChartData()
    test.test()
    # test.description()