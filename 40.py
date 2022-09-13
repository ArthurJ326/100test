# ：将一个数组逆序输出。
#
# 程序分析：用第一个与最后一个交换。
#
# 程序源代码：
import copy

a = [1, 3, 4, 5, 6, 8, 9, 10]
b = []
b = copy.deepcopy(a)
b.reverse()
print(a)
print(b)
