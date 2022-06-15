# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 20:11
# @Author : Cosmica
# @File : 匹配目标并提取
# @Project : Spider
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
# 调用 group 方法并传入索引，提取要匹配的目标
print(result.group(1))
print(result.span())
