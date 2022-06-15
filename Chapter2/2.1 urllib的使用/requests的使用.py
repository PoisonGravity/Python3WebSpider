# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 15:52
# @Author : Cosmica
# @File : requests的使用
# @Project : Spider


# P48
"""
requests
在处理网页验证和 Cookie 时，需要写 Opener 类和 Handler 类来处理
另外实现 POST 和 GET 请求的写法也不太方便
为了更方便的实现这些操作，产生了更强大的库：requests
安装：pip3 install requests
"""
# 例子：
import requests

r = requests.get('https://www.baidu.com/')
# r = requests.post('https://www.httpbin.org/get')
# r = requests.post('https://www.httpbin.org/post')
# r = requests.post('https://www.httpbin.org/put')
# r = requests.post('https://www.httpbin.org/delete')
# r = requests.post('https://www.httpbin.org/patch')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text[:100])
print(r.cookies)
