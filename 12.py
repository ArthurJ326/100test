# 题目：判断101-200之间有多少个素数，并输出所有素数。
#
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数。
from math import sqrt
from sys import stdout

for A in range(101, 200):

    for B in range(2, A):

        if A % B == 0:
            break
    else:

        print(A)

# from math import sqrt
#
# count=0
# pn=1
# for i in range(101,201):
#   k=int(sqrt(i))
#   for j in range(2,k+1):
#       if i%j==0:
#             pn=0
#             break
#       if pn==1:
#         count+=1
#         print (i)
#       pn=1
# print(f"total number is {count:d}")
