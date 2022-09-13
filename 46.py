# 求输入数字的平方，如果平方运算后小于 50 则退出。
#
# 程序分析：无


while True:
    a = int(input("请输入数字"))

    b= a **2
    print(f"输入数字的平方为{b}")
    if b <= 50:
        print("数字不满足条件")

        break
