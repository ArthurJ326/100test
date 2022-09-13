# MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
# MINIMUM = lambda x, y: (x > y) * y + (x < y) * x
#
# if __name__ == '__main__':
#     a = 10
#     b = 20
#     print('The largar one is %d' % MAXIMUM(a, b))
#
#     print('The lower one is %d' % MINIMUM(a, b))

a = 10
b = 20
if (a>b)*a ==0 and (a<b)*b ==20:
    print("a>b")
elif (a<b)*b ==20:
    print("a<b 为1")