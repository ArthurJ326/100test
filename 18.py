# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#
# 程序分析：关键是计算出每一项的值。
a = 0
S = 0
num = int(input("请输入要相加的数字"))
num_1 = num
times = int(input("请输入要相加的次数"))
print(f"{num_1} +",end=" ")
if times == 1:
    S = num

else:
    for T in range(1,times):
        if T != times-1:
            x = 10**T
            num = num_1*x+num
            print(f"{num} + ", end=" ")
            S += num
        elif T == times-1:
            x = 10 ** T
            num = num_1 * x + num
            print(f"{num}  ", end=" ")
            S += num



print(f"相加的总数为{S}")





