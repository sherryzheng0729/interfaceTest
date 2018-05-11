# import pymysql
# #连接数据库
# conn = pymysql.connect(host='192.168.1.152',port= 3306,user = 'root',passwd='123123',db='test') #db：库名
# #设置游标类型，默认游标类型为元祖形式
# #将游标类型设置为字典形式
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cur.execute("select * from lcj")  #逼表中所有的操作都可以再此进行操作
# #将lcj表中所有数据以字典形式输出
# ret = cur.fetchall()
# print(ret)   #[{'age': 18, 'tel': '13520617734', 'name': 'xiaoluo', 'id': 1, 'sex': '?'},
# #提交
# conn.commit()
# #关闭指针对象
# cur.close()
# #关闭连接对象
# conn.close()

test=[]
print(type(test))