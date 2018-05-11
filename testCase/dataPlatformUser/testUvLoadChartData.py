import unittest

import readConfig
from common import configHttp, configDB, common
from common.Log import MyLog

localConfigHttp = configHttp.ConfigHttp()
localReadConfig = readConfig.ReadConfig()
localConfigDB = configDB.MyDB()

class UvLoadChartData(unittest.TestCase):



    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def setParameters(self, endTime, stats, type, name):
        self.startTime = "2018-05-11"
        self.endTime = str(endTime)
        self.stats = str(stats)
        self.type = str(type)
        self.name = str(name)

    def interfaceTest(self):
        # set url
        self.url = common.get_url_from_xml('dataPlatformUser_loadChartData')
        localConfigHttp.set_url(self.url)
        # set header
        cookie = localReadConfig.get_headers("cookie")
        contentType = localReadConfig.get_headers("contentType")
        header = {"Content-Type": contentType, "Cookie": cookie}
        localConfigHttp.set_headers(header)
        self.setParameters("2018-05-11","user","time","uv")
        # set params
        data = {
                'endTime': self.endTime,
                'stats': self.stats,
                'type': self.type,
                'name': self.name}
        localConfigHttp.set_data(data)

        # test interface
        self.response = localConfigHttp.post()
        self.info = self.response.json()
        common.show_return_msg(self.response)

    def excuteSQL(self):
        pass

    def testUvLoadChartData_today(self):
        self.interfaceTest()

    def tearDown(self):
        pass

if __name__ == '__main__':
    test = UvLoadChartData()
    # test.setParameters()
    test.testUvLoadChartData_today()