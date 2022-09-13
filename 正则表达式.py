"""
. 表示要匹配除了 换行符 之外的任何 单个 字符。

比如，你要从下面的文本中，选择出所有的颜色。





* 表示匹配前面的子表达式任意次，包括0次。

比如，你要从下面的文本中，选择每行逗号后面的字符串内容，包括逗号本身。注意，这里的逗号是中文的逗号。



+ 表示匹配前面的子表达式一次或多次，不包括0次。

比如，还是上面的例子，你要从文本中，选择每行逗号后面的字符串内容，包括逗号本身。

但是 添加一个条件， 如果逗号后面 没有内容，就不要选择了。

比如，下面的文本中，最后一行逗号后面 没有内容，就不要选择了。

{}花括号表示 前面的字符匹配 指定的次数 。

比如 ，下面的文本

红彤彤，绿油油，黑乎乎，绿油油油油
表达式 油{3} 就表示匹配 连续的 油 字 3次

表达式 油{3,4} 就表示匹配 连续的 油 字 至少3次，至多 4 次




"""

import re

# context="""
#            苹果是黑色的
#            橙子是橙色的
#            香蕉是黄色的
#            乌鸦是黑色的"""
#
# lines = re.compile(r'.色')
# for one in lines.findall(context):
#
#     print(one)
context = """
           苹果，是黑色的
           橙子，是橙色的
           香蕉，是黄色的
           乌鸦，是黑色的
           猴子，
        """
lines = re.compile(r'，.*')  # .表示一个任意字符 *表示任意个字符 ，如果开头的确认了，后面全要的话 用.* 要几个可以打几个.点
for one in lines.findall(context):
    print(one)

context_1 = """红彤彤，绿油油，黑乎乎，绿油油油油"""

context_2 = re.compile(r'绿油{4}')
for two in context_2.findall(context_1):
    print(two)

source = '<html><head><title>Title</title>'
p = re.compile(r"<.*?>")  # +和* 都是贪婪的 ，在他们之后加？后会变成非贪婪模式，能以最少的匹配 当在发现第一个>后就匹配
for c in p.findall(source):
    print(c, end="\t\n")

content = '''001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80'''

j = re.compile(r"^\d+", re.M)
for a in j.findall(content):
    print(a)
k = re.compile(r"\d+$", re.M)
for b in k.findall(content):
    print(b)

content = '''苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的'''
l = re.compile(r"^(.+)，(.+色)", re.M)
for c in l.findall(content):
    print(c)

names = '''

下面是这学期要学习的课程：

<a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是牛顿第2运动定律

<a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是毕达哥拉斯公式

<a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是切割磁力线
'''


def subfunc(aaaa):
    src = aaaa.group(0)  # 0代表 找到的对象
    number_1 = int(aaaa.group(1)) + 6  # match 对象 group（1） 代表是第一个group的分组 r"^(这就是第一个group)(第二个)"
    dest = f"/av{number_1}/"
    print(f"把{src}替换为{dest}")
    return dest


d = re.sub(r"/av(\d*?)/", subfunc, names) # 可以用函数也可以用固定值
# d = re.sub(r"/av(\d*?)/", "/cn345677/", names)
print(d)