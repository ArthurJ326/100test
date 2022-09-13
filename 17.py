# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#
# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
#
input_words = str(input("请输入您所想要的字符"))

words = 0
num=0
space=0
others = 0


for x in input_words:
    if x.isalpha():
        words += 1

        pass
    elif x.isnumeric():
        num += 1
        pass

    elif x.isspace():
        space += 1
        pass

    else:
        others += 1

print(f"输入的字符中字母有{words}个,数字有{num}个,空格有{space}个，其他字符个数为{others}")
