# 对10个数进行排序。
#
# 程序分析：可以利用选择法，即从后9个比较过程中
# ，选择一个最小的与第一个元素交换，下次类推，
# 即用第二个元素与后8个进行比较，并进行交换。

a = [6, 5, 8, 98, 56, 485, 785, 12, 12, 456, 1258, 14558, 5547]

a.sort()
b = a
b.reverse()
print(a)
print(b)