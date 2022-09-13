# 求100之内的素数
a = 0
b = []
for c in range(2, 101):
    for d in range(2, c):
        if c % d == 0:
            break
    else:
        b.append(c)

print(b)
