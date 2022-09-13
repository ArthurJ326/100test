# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
input_words = input("input a string:")


def output_words(x, l):
    if l == 0:
        return "结束了"
    print(x[l-1]) # 如果三个数的话应该下标为0，1，2 所以要-1
    output_words(x, l - 1)

output_words(input_words, len(input_words))
