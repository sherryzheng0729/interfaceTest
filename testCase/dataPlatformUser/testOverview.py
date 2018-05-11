import unittest

import requests

import readConfig
from common import configHttp, configDB, common
from common.Log import MyLog

localConfigHttp = configHttp.ConfigHttp()
localReadConfig = readConfig.ReadConfig()
localConfigDB = configDB.MyDB()


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
        self.todayTurnoverUsers = self.info['data']['todayTurnoverUsers']
        self.todayTurnoverUsersRate = self.info['data']['todayTurnoverUsersRate']
        self.todayUv = self.info['data']['todayUv']
        self.todayUvRate = self.info['data']['todayUvRate']
        self.totalTurnoverUsers = self.info['data']['totalTurnoverUsers']
        self.totalUv = self.info['data']['totalUv']
        self.turnoverUsersRate = self.info['data']['turnoverUsersRate']
        self.uvRate = self.info['data']['uvRate']

    def excuteSQL(self):
        # get sql
        sqltodayTurnoverUsers = common.get_sql('shop-v2','t_pv','Overview','todayTurnoverUsers')
        self.sqltodayTurnoverUsersRate = common.get_sql('shop-v2', 't_pv', 'Overview','todayTurnoverUsersRate')
        self.sqltodayUv = common.get_sql('shop-v2', 't_pv','Overview', 'todayUv')
        self.sqltodayUvRate = common.get_sql('shop-v2', 't_pv','Overview', 'todayUvRate')
        self.sqltotalTurnoverUsers = common.get_sql('shop-v2', 't_pv','Overview', 'totalTurnoverUsers')
        self.sqltotalUv = common.get_sql('shop-v2', 't_pv','Overview', 'totalUv')
        self.sqlturnoverUsersRate = common.get_sql('shop-v2', 't_pv', 'Overview','turnoverUsersRate')
        self.sqluvRate = common.get_sql('shop-v2', 't_pv', 'Overview','uvRate')
        localConfigDB.connectDB()
        self.expect1 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqltodayTurnoverUsers))[0][0]
        print(1+self.expect1)
        self.expect2 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltodayTurnoverUsersRate))[0][0]
        print(2+self.expect2)
        self.expect3 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltodayUv))[0][0]
        self.expect4 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltodayUvRate))[0][0]
        self.expect5 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltotalTurnoverUsers))[0][0]
        self.expect6 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqltotalUv))[0][0]
        self.expect7 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqlturnoverUsersRate))[0][0]
        self.expect8 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(self.sqluvRate))[0][0]
        localConfigDB.closeDB()
        print("close")

    def testOverview_todayTurnoverUsers(self):
        self.interfaceTest()
        self.excuteSQL()
        # check result
        self.assertEqual(self.todayTurnoverUsers,self.expect1)

    def testOverview_todayTurnoverUsersRate(self):
        self.interfaceTest()
        self.excuteSQL()
        # check result
        self.assertEqual(self.todayTurnoverUsersRate,self.expect2)

    def testOverview_todayUv(self):
        self.interfaceTest()
        self.excuteSQL()
        # check result
        self.assertEqual(self.todayUv,self.expect3)

    def testOverview_todayUvRate(self):
        self.interfaceTest()
        self.excuteSQL()
        # check result
        self.assertEqual(self.todayUvRate,self.expect4)

    def testOverview_totalTurnoverUsers(self):
        self.interfaceTest()
        self.excuteSQL()
        # check result
        self.assertEqual(self.totalTurnoverUsers,self.expect5)

    def testOverview_totalUv(self):
        self.interfaceTest()
        self.excuteSQL()
        # check result
        self.assertEqual(self.totalUv,self.expect6)

    def testOverview_turnoverUsersRate(self):
        self.interfaceTest()
        self.excuteSQL()
        # check result
        self.assertEqual(self.turnoverUsersRate,self.expect7)

    def testOverview_uvRate(self):
        self.interfaceTest()
        self.excuteSQL()
        # check result
        self.assertEqual(self.uvRate,self.expect8)



    def tearDown(self):
        pass


if __name__ == '__main__':
    test = overview()
    test.testOverview_todayTurnoverUsers()
    test.testOverview_todayUvRate()
    test.testOverview_uvRate()
    # test.testOverview_todayTurnoverUsersRate()


