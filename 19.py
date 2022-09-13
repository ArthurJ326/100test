# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。
#
# 程序分析：请参照程序Python 练习实例14。
import functools

# nums_input = int(input("请输入一个正整数: "))
# nums = nums_input
# print(f"{nums} = ", end=" ")

# 因子之和等于其本身，那这个数首先一定是个质因数，先找质因数
x = []
# while nums != 1:
for f in range(2, 1001):
    for j in range(1, f):

        if f % j == 0:
            # nums = int(nums / f)
            x.append(j)
        # if nums == 1:
        #     print(f"{f}", end=" ")
        # else:
        #     print(f"{f}*", end=" ")
    if f == functools.reduce(lambda a, b: a + b, x):
        print(f"\n{f}")
    x = []
