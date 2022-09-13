# 给一个不多于5位的正整数，
# 要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。


a = input("输入一个5位以内的正整数:")
c = []
numbers_1 = len(a)

print(f"该数共有{numbers_1}位")

for b in a:
    c.append(b)

c.reverse()
print(c)
