# 打印出如下图案（菱形）:
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
"""
打印行数是7 ， 最多一行的 * 数量与行数是相等的

"""
x = 7
for a in range(1, x + 1, 2):
    if a == 1:
        print(" "*int(x/2),end="")
        print("*")
    elif a >= 1:
        print(" " * int((x-a)/2), end="")
        print("*" * a)
for a in range(x-2, 0, -2):
    if a == 1:
        print(" " * int(x/2-2), end="")
        print(" ","*")
    elif a > 1:
        print(" " * int((x - a) / 2), end="")
        print("*" * a)
