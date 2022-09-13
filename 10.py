# 题目：暂停一秒输出，并格式化当前时间。
import time

A = 0
print(A)

time.sleep(2)

print(time.strftime("%Y-%m-%d-%H-%M-%S"))  # Y 大写  D M S 分钟都要大写
