import unittest

import requests

import readConfig
from common import configHttp, configDB, common
from common.Log import MyLog

localConfigHttp = configHttp.ConfigHttp()
localReadConfig = readConfig.ReadConfig()
localConfigDB = configDB.MyDB()
localConfigDB.connectDB()

class overview(unittest.TestCase):

    def setup(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def interfaceTest(self):
        # set url
        self.url = common.get_url_from_xml('dataPlatformUser_overview')
        localConfigHttp.set_url(self.url)
        # set header
        cookie = localReadConfig.get_headers("cookie")
        contentType = localReadConfig.get_headers("contentType")
        header = {"Content-Type": contentType, "Cookie": cookie}
        localConfigHttp.set_headers(header)
        # test interface
        self.response = localConfigHttp.post()
        self.info = self.response.json()
        common.show_return_msg(self.response)

    def testOverview_todayTurnoverUsers(self):
        self.interfaceTest()
        self.todayTurnoverUsers = self.info['data']['todayTurnoverUsers']
        sqltodayTurnoverUsers = common.get_sql('shop-v2', 't_pv', 'Overview', 'todayTurnoverUsers')
        self.expect = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqltodayTurnoverUsers))[0][0]
        # check result
        self.assertEqual(self.todayTurnoverUsers,self.expect)


    def testOverview_todayTurnoverUsersRate(self):
        self.interfaceTest()
        self.todayTurnoverUsersRate = self.info['data']['todayTurnoverUsersRate']
        self.sqltodayTurnoverUsersRate = common.get_sql('shop-v2', 't_pv', 'Overview', 'todayTurnoverUsersRate')
        self.expect = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltodayTurnoverUsersRate))[0][0]
        # check result
        self.assertEqual(self.todayTurnoverUsersRate,self.expect)

    def testOverview_todayUv(self):
        self.interfaceTest()
        self.todayUv = self.info['data']['todayUv']
        self.sqltodayUv = common.get_sql('shop-v2', 't_pv', 'Overview', 'todayUv')
        self.expect = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltodayUv))[0][0]
        # check result
        self.assertEqual(self.todayUv,self.expect)

    def testOverview_todayUvRate(self):
        self.interfaceTest()
        self.todayUvRate = self.info['data']['todayUvRate']
        self.sqltodayUvRate = common.get_sql('shop-v2', 't_pv', 'Overview', 'todayUvRate')
        self.expect = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltodayUvRate))[0][0]
        # check result
        self.assertEqual(self.todayUvRate,self.expect)

    def testOverview_totalTurnoverUsers(self):
        self.interfaceTest()
        self.totalTurnoverUsers = self.info['data']['totalTurnoverUsers']
        self.sqltotalTurnoverUsers = common.get_sql('shop-v2', 't_pv', 'Overview', 'totalTurnoverUsers')
        self.expect = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltotalTurnoverUsers))[0][0]
        # check result
        self.assertEqual(self.totalTurnoverUsers,self.expect)

    def testOverview_totalUv(self):
        self.interfaceTest()
        self.totalUv = self.info['data']['totalUv']
        self.sqltotalUv = common.get_sql('shop-v2', 't_pv', 'Overview', 'totalUv')
        self.expect = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltotalUv))[0][0]
        # check result
        self.assertEqual(self.totalUv,self.expect)

    def testOverview_turnoverUsersRate(self):
        self.interfaceTest()
        self.turnoverUsersRate = self.info['data']['turnoverUsersRate']
        self.sqlturnoverUsersRate = common.get_sql('shop-v2', 't_pv', 'Overview', 'turnoverUsersRate')
        self.expect = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqlturnoverUsersRate))[0][0]
        # check result
        self.assertEqual(self.turnoverUsersRate,self.expect)

    def testOverview_uvRate(self):
        self.interfaceTest()
        self.uvRate = self.info['data']['uvRate']
        self.sqluvRate = common.get_sql('shop-v2', 't_pv', 'Overview', 'uvRate')
        self.expect = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqluvRate))[0][0]
        localConfigDB.closeDB()
        # check result
        self.assertEqual(self.uvRate,self.expect)


    def tearDown(self):
        pass

if __name__ == '__main__':
    test = overview()
    test.testOverview_todayTurnoverUsers()
    test.testOverview_todayTurnoverUsersRate()
    localConfigDB.closeDB()


