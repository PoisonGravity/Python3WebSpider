# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 23:41
# @Author : Cosmica
# @File : search
# @Project : Spider


# P69
# search
"""
前面提到的：match 方法是从字符串的开头开始匹配的
这意味着一旦开头不匹配，整个匹配就失败了
为此，我们可以使用 search 方法
search 方法：它在匹配时会扫描整个字符串，然后返回第一个匹配成功的结果
"""
# 下面这个是使用 match 方法的例子
# import re
#
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.match('Hello.*?(\d+).*?Demo', content)
# print(result)   # 打印 None


# 将 match 方法改为 search 方法：
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)   # 打印 None


