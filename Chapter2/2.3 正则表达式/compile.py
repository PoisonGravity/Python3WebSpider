# _*_ coding : utf-8 _*_
# @Time : 2022/6/16 17:07
# @Author : Cosmica
# @File : compile
# @Project : Spider


# P73
# compile
"""
有可能有多个地方使用同一个正则表达式
这时我们可以利用 compile 将正则表达式编译成一个对象
这样方便复用
"""
import re

content1 = '2019-12-15 12:00'
content2 = '2019-12-17 12:55'
content3 = '2019-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
