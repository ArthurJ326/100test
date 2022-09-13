# 利用递归方法求5!。
#
# 程序分析：递归公式：fn=fn_1*4

def fact(j):
    if j == 1:
        return 1
    else:
        sum_total = fact(j - 1) * j
        return sum_total


x = fact(3)
print(x)
