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
# import requests
#
# r = requests.get('https://www.baidu.com/')
# # r = requests.post('https://www.httpbin.org/get')
# # r = requests.post('https://www.httpbin.org/post')
# # r = requests.post('https://www.httpbin.org/put')
# # r = requests.post('https://www.httpbin.org/delete')
# # r = requests.post('https://www.httpbin.org/patch')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text[:100])
# print(r.cookies)


# GET 请求
# 例子
# import requests
# # 在 URL 中添加参数
# # 优雅的方式：
# data = {
#     'name': 'germey',
#     'age': '25'
# }
# r = requests.get('https://www.httpbin.org/get', params=data)
# print(r.text)


# 抓取网页
# 例子：
# import requests
# import re
#
# r = requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


# 抓取二进制数据(图片、音频、视频)
# import requests
#
# r = requests.get('https://scrape.center/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
# # print(r.text)
# # print(r.content)


# 添加请求头
# 例子：
# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
# }
# r = requests.get('https://ssr1.scrape.center/', headers=headers)
# print(r.text)


# POST 请求
# 例子
import requests
data = {'name': 'germey', 'age': '25'}
r = requests.post("https://www.httpbin.org/post", data=data)
print(r.text)


# 文件上传
