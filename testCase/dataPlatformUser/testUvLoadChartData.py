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

    def description(self):
        self.case_name

    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()


    def interfaceTest(self):
        # set url
        self.url = common.get_url_from_xml('dataPlatformUser_loadChartData')
        localConfigHttp.set_url(self.url)
        # set header
        cookie = localReadConfig.get_headers("cookie")
        contentType = localReadConfig.get_headers("contentType")
        header = {"Content-Type": contentType, "Cookie": cookie}
        localConfigHttp.set_headers(header)

        # 不稳定，暂不用
        # if str(self.startTime) == str('today'):
        #     self.start = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        # else:
        #     self.start = self.startTime

        # set data
        data = {
                'startTime': self.startTime,
                'endTime': self.endTime,
                'stats': self.stats,
                'type': self.type,
                'name': self.name}
        localConfigHttp.set_data(data)

        # test interface
        self.response = localConfigHttp.postWithJson()
        self.info = self.response.json()
        common.show_return_msg(self.response)
        common.get_value_from_return_json(self.info,"series",data)

    def excuteSQL(self):
        pass

    def testUvLoadChartData_today(self):
        self.interfaceTest()

    def tearDown(self):
        pass

if __name__ == '__main__':
    test = UvLoadChartData()
    test.testUvLoadChartData_today()


