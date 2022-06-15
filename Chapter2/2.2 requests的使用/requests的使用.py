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
# import requests
# data = {'name': 'germey', 'age': '25'}
# r = requests.post("https://www.httpbin.org/post", data=data)
# print(r.text)


# 文件上传
# import requests
#
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('https://www.httpbin.org/post', files=files)
# print(r.text)


# Cookie 获取
# 例子1：
# import requests
#
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + "=" + value)

# 例子2：
# import requests
#
# headers = {
#     'cookie': '_octo=GH1.1.2133112272.1649413925; tz=Asia%2FShanghai; _device_id=3f76259ba6a9560b3c09c8ebbc19e0a7; user_session=0KW9eFkKJYzIP8o0OOmo7tRC_JFa_3lUl0I872xVkA1mkozv; __Host-user_session_same_site=0KW9eFkKJYzIP8o0OOmo7tRC_JFa_3lUl0I872xVkA1mkozv; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22dark%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=Lucid1ty; has_recent_activity=1; _gh_sess=323MBuo3IWPPXhEnq9x5A%2FT%2BjRD00J4Y057K1NsmhYoIDg1apw2NgHs%2BgRiPbFwXIaql7E2ZJlm0OlsyROBXx5BIrEGJi2R6wDnQ8NsA5tepgkLY4NkZ4xKaPE%2FOJtsu1ya9AgF4lCl12QTCbc%2B75IDLuEo8XABnbUhCmZD%2BE6FyrhV9KTOEgVJQ6IK36j99AY7eFatJNC2ExohIHi6BYCKh55WA5voYTr4zd2et3RO4vAqX6fvVqEeL3Dc4x2xoMaDWQvSinsdOkNMDAGsIovHPW7%2FQiDV1C1Fy3A%3D%3D--Pv8pjirHpmQDEsrZ--NmaBaQjJWDNzEjz7ht7ESw%3D%3D',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
# }
# r = requests.get('https://github.com', headers=headers)
# print(r.text)


# Session 维持
"""
场景：
第一个请求利用 requests 库的 post 方法登录了某个网站，第二次想要获取成功登录后的自己的个人信息
于是又用了一次 requests 库的 get 方法去请求个人页面信息
这实际上相当于打开了两个浏览器，是互相独立的，对应完全不相关的 Session
那么第二次的请求就获取不到个人信息
解决办法：Session对象
"""
# 沿用之前的写法：
# import requests
#
# requests.get('https://www.httpbin.org/cookies/set/number/123456789')
# r = requests.get('https://www.httpbin.org/cookies')
# print(r.text)   # 得到的 cookies 是空的


# 利用 Session
# import requests
#
# s = requests.Session()
# s.get('https://www.httpbin.org/cookies/set/number/123456789')
# r = s.get('https://www.httpbin.org/cookies')
# print(r.text)   # Cookie 被成功获取！


# SSL 证书验证
# import requests
# import logging
# from requests.packages import urllib3 # 这里报错，不知道为什么
#
# # 捕获警告到日志中从而忽略警告
# logging.captureWarnings(True)
#
#
# # 另一种方式忽略警告
# # urllib3.disable_warnings()
#
# # 在 get 方法中填入参数：verify=False 可以忽略网站证书的验证
# response = requests.get('https://ssr2.scrape.center/', verify=False)
# print(response.status_code)


# 超时设置
# import requests
# # 只需要在 get 方法中添加 timeout 参数即可
# r = requests.get('https://www.httpbin.org/get', timeout=0.1)
# print(r.status_code)


# 身份认证
# 例子1：
# import requests
# from requests.auth import HTTPBasicAuth
#
# r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# print(r.status_code)


# 例子1更简单的写法：
# import requests
# # 直接传一个元组，它会默认使用 HTTPBasicAuth 这个类来认证
# r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# print(r.status_code)


# 使用 OAuth 认证
# 先安装：pip3 install requests_oauthlib
import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)





