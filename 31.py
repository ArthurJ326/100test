# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。

import re

list_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

find_word = input("please input the first word :")
g = []
for f in list_week:

    if re.match(find_word, f):
        g.append(f)
        continue
if len(g) == 1:
    print(g[0])


else:
    b = input("请输入第二个字符")
    for c in list_week:
        q = b
        if re.match(find_word + q, c):
            print(c)
            continue


