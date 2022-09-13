# 印出杨辉三角形（要求打印出10行如下图）。　　
#
# 程序分析：无。
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1


x = 10


def lst(i, j):
    if i == j :
        return 1

    elif j == 1:
        return 1

    else:
        return lst(i - 1, j - 1) + lst(i - 1, j)


for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(lst(i, j),end=" ")
        if i == j :
            print()
