# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 20:11
# @Author : Cosmica
# @File : 匹配目标并提取
# @Project : Spider


# P66
# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# # 调用 group 方法并传入索引，提取要匹配的目标
# print(result.group(1))  # group(1) 表示输出第一个被()匹配的结果
# print(result.span())


# P67
# 通用匹配：.* 匹配任意字符(可以简化正则表达式的书写)
# import re
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())


# P67
# 贪婪与非贪婪
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))


