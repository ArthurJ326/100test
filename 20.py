# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，TODO 共经过多少米？第10次反弹多高？
#
# 程序分析：无

"""
每次落下是一半 ，当原高度是X ，X/2  X/4 X/8
    总共落下多少可以放在list里求和

 """
high = 100
count = 10
total = []
length = []
for c in range(1, 11):
    x = 2 ** c
    int_high = high / x
    length.append(int_high)

    total.append(int_high * 2)

print(f"{length[-1]}")
print(f"{sum(total) + 100}")  # 加上第一次的100
