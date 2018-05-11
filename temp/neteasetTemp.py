# self.url=url
# self.headers = {"Content-Type": "application/json; charset=UTF-8",
#                 "Cookie": "NASA-ADMIN-SESSION=69d66497-cf02-4516-a5f9-ef7f6c532bd9"}
# r = requests.post(url=self.url, headers=self.headers, verify=False)
# print(r.json())
# return r.json()

#
# def db_query(self):
#     self.connectDB()
#     sql = "select sum(uv) from (SELECT count(distinct uid) as uv,from_unixtime(ct/1000,'%Y-%m-%d') as days FROM `shop-v2`.t_pv group by days) as temp"
#     # print(sql)
#     self.cur.execute(sql)
#     result_query = self.cur.fetchone()
#     sum_query = result_query[0]
#     print(sum())
#     return sum_query
from common import configDB

localConfigDB = configDB.MyDB()
class testsql():

    def db_query(self):
        localConfigDB.connectDB()
        sql = "select sum(uv) as totalUv from(SELECT count(distinct uid) as uv,from_unixtime(ct/1000,'%Y-%m-%d') as days FROM `shop-v2`.t_pv group by days) as temp;"
        # print(sql)
        # self.cur.execute(sql)
        cur = localConfigDB.executeSQLNoParam(sql)
        #result_query = self.cur.fetchone()
        result_query = localConfigDB.get_all(cur)
        sum_query = result_query[0]
        print(sum_query)
        localConfigDB.closeDB()
        return sum_query


if __name__ == '__main__':
    test = testsql()
    test.db_query()

# localConfigDB.executeSQLNoParam(sqltodayTurnoverUsers)
        # expect1 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqltodayTurnoverUsers))[0][0]
        # # print(expect1)
        # self.assertEqual(todayTurnoverUsers,expect1)

        # localConfigDB.executeSQLNoParam(sqltodayTurnoverUsers)
        # expect2 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqltodayTurnoverUsersRate))[0][0]
        # self.assertEqual(todayTurnoverUsersRate,expect2)
        #
        # localConfigDB.executeSQLNoParam(sqltodayUv)
        # expect3 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqltodayUv))[0][0]
        # self.assertEqual(todayUv, expect3)
        #
        # localConfigDB.executeSQLNoParam(sqltodayUvRate)
        # expect4 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqltodayUvRate))[0][0]
        # self.assertEqual(todayUvRate, expect4)
        #
        # localConfigDB.executeSQLNoParam(sqltotalTurnoverUsers)
        # expect5 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqltotalTurnoverUsers))[0][0]
        # self.assertEqual(totalTurnoverUsers, expect5)
        #
        # localConfigDB.executeSQLNoParam(sqltotalUv)
        # expect6 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqltotalUv))[0][0]
        # self.assertEqual(totalUv, expect6)
        #
        # localConfigDB.executeSQLNoParam(sqlturnoverUsersRate)
        # expect7 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqlturnoverUsersRate))[0][0]
        # self.assertEqual(turnoverUsersRate, expect7)
        #
        # localConfigDB.executeSQLNoParam(sqluvRate)
        # expect8 = localConfigDB.get_all(localConfigDB.executeSQLNoParam(sqluvRate))[0][0]
        # self.assertEqual(uvRate, expect8)