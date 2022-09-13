# 暂停一秒输出。
#
# 程序分析：使用 time 模块的 sleep() 函数。
import time

A = int(input("请输入所需要的数字："))

print(A)

time.sleep(2) # 参数是秒

print(A+2)