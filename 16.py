# 输出指定格式的日期。
#
# 程序分析：使用 datetime 模块。

import datetime

# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
a = datetime.date.today().strftime("%d/%m/%Y")
print(a)
# 创建日期对象
b = datetime.datetime(1990, 3, 26, 12, 10, 33,2222)
print(b.strftime("%f/%S/%M/%H/%d/%m/%Y"))

c = datetime.date.today()
d =c+ datetime.timedelta()
print(d)