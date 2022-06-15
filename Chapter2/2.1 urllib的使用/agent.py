# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 14:32
# @Author : Cosmica
# @File : agent
# @Project : Spider
# P36
# 为爬虫添加代理
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
# 这里需要事先在本地搭建一个 HTTP 代理，并让其运行在8080端口上
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080',
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
