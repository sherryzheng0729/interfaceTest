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
