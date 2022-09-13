# 求一个3*3矩阵主对角线元素之和。
#
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
#
# 程序源代码：
"""
1   2    3

4   5    6

7   8    9

"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum_total = 0
if input("请选择计算的模式/或\\") == "\\":
    for b in range(0, 3):
        sum_total += matrix[b][b]
else:
    d = 2
    for c in range(0, 3):

        sum_total += matrix[c][d]
        d -= 1


print(sum_total)
