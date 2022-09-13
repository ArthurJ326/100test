# 题目：输入某年某月某日，判断这一天是这一年的第几天？
#
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
# 1，判断是否是闰年
months_days = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
months_day = 0
total_days = 0
if month in range(0, 13):
    months_day = months_days[month - 1]+day
    # print(months_day)

# 1，判断是否是闰年
total_days = months_day
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    if month > 2:
        total_days = months_day + 1
    else:
        total_days = months_day

print(total_days)
