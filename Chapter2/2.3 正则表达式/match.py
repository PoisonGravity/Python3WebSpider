# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 20:04
# @Author : Cosmica
# @File : match
# @Project : Spider
# P66
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())
