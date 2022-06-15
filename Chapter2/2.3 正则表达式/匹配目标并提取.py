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
"""
下面这个例子想要匹配1234567这些数字，但是只匹配到了7这一个数字
原因是：使用：.* 匹配，它是贪婪的，会尽可能多的去匹配符合的字符
这里它把123456都匹配了，只留下了7给\d+去匹配数字
要解决的话，使用：.*? 即可，多加了一个问号，这样就是非贪婪的
但是要注意：如果要匹配的结果在字符串的末尾，则.*?可能匹配不到任何内容！
"""
import re

content = 'Hello 1234567 World_This is a Regex Demo'
# .* 与 .*?
result = re.match('^He.*?(\d+).*?Demo$', content)
print(result)
print(result.group(1))


