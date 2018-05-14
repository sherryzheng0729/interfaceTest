# @classmethod的使用
# class A(object):
#     bar = 1
#
#     def func1(self):
#         print('foo')
#
#     @classmethod
#     def func2(cls):
#         print('func2')
#         print(cls.bar)
#         cls().func1()

# A.func2()
jsonTest = {
    "code": 0,
    "data": {
        "series": [
            {
                "data": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ],
                "name": "今日"
            },
            {
                "data": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ],
                "name": "昨日"
            },
            {
                "data": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0.14,
                    0,
                    0,
                    0,
                    0,
                    0.14,
                    0,
                    0,
                    0,
                    0.14,
                    0,
                    0.14,
                    0,
                    0
                ],
                "name": "历史7日均值"
            }
        ],
        "time": [
            "00:00",
            "01:00",
            "02:00",
            "03:00",
            "04:00",
            "05:00",
            "06:00",
            "07:00",
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00"
        ]
    },
    "msg": "Ok"
}
todaylist=jsonTest["data"]["series"][0]["data"]
print(type(todaylist.__len__()))

num = 0
for i in todaylist.__len__():
    while todaylist[i] == 0:
        num+=1
if num == todaylist.__len__():
    print("all 0")
