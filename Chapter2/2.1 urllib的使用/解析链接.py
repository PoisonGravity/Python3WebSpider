# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 15:30
# @Author : Cosmica
# @File : 解析链接
# @Project : Spider


# P40
"""
urlparse
该方法可以实现 URL 的识别和分段
"""
# 例子：
from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
