# 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
#
# 程序分析：无。


from collections import deque
import re
m = 3
a = [1, 2, 3, 4, 5, 6, 7]  # 7 个数
# f = deque(a)
# f.rotate()
g = a.index(3)
a.append(a.pop(2))
print(a)
print (list(f))
