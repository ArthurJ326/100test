# 一个5位数，判断它是不是回文数。
# 即12321是回文数，个位与万位相同，十位与千位相同。
#
# 程序分析：无。
a = input("输入一个5位以内的正整数:")
c = []
d = int(len(a) / 2)
e = 0
for b in a:
    c.append(b)
for x in range(d):
    if c[0 + x] == c[-1 - x]:
        e += 1
if e == d:
    print("这个数是回文数")

else:
    print("非回文数")
