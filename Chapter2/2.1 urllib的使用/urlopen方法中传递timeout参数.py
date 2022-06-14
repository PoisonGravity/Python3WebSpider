# _*_ coding : utf-8 _*_
# @Time : 2022/6/14 23:51
# @Author : Cosmica
# @File : urlopen方法中传递timeout参数
# @Project : Spider
import socket
import urllib.request
import urllib.error
# try except 语句捕获并处理异常
try:
    # 设置 timeout 为0.1秒
    response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
# 当程序运行超过0.1秒还没有响应则会抛出 urllib.error.URLError,这是一个URLError异常,该异常属于 urllib.error模块
# print(response.read())
