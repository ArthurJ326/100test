# 求1+2!+3!+...+20!的和。
#
# 程序分析：此程序只是把累加变成了累乘。

"""
x=1*2*3.....*x


"""
s = 0
for x in range(1, 21):
    a = 1
    for i in range(1, x + 1):
        a *= i
    s = s + a
print(s)
