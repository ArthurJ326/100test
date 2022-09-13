# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def calculate(n):
    s = [1/i for i in range(2,n+1,2)]
    return sum(s)
def calculate_1(n):
    s = [1/i for i in range(1,n+1,2)]
    return sum(s)
# def calculate(n):  倒叙同时适用于奇数和偶数
#     s = [1/i for i in range(n,0,-2)]
#     return sum(s)
print(calculate(6))
print(calculate_1(5))