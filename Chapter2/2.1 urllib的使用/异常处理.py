# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 14:47
# @Author : Cosmica
# @File : 异常处理
# @Project : Spider


# P38
"""
URLError
由 request 模块产生的异常都可以通过捕获 URLError 这个类来处理
它具有一个属性 reason，即返回错误的原因
"""
# 例子：
# from urllib import request, error
#
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except error.URLError as e:
#     print(e.reason)


"""
HTPError
HTPError 是 URLError 的子类，专门处理 HTTP 请求错误，例如认证失败等
它有三个属性：code(状态码) reason(错误的原因) headers(请求头)
"""
# 例子
from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/404')
# 因为 URLError 是 HTTPError 的父类，所以可以先选择捕获子类的错误再捕获父类的错误
# 更好的写法如下
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
# 最后用 else 语句处理正常的逻辑
else:
    print('Request Successfully')
