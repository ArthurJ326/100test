# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
#
# 程序分析：请抓住分子与分母的变化规律。
"""
先确定分子，分母 x/y y+x/x
循环20次
求和

"""

x = 2
y = 1
total = 0
for n in range(1, 21):
    total = x / y + total
    c = x
    x = y + x
    y = c

print(total)
