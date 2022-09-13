# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，60分以下的用C表示。
#
# 程序分析：程序分析：(a>b) ? a:b 这是条件运算符的基本例子。
score = int(input("请输入分数"))
if 0 < score:

    if score >= 90:
        print("A")
    elif 60 < score < 89:
        print("B")
    else:
        print("C")
else:
    print("请输入正确分数")
