# _*_ coding : utf-8 _*_
# @Time : 2022/6/16 17:12
# @Author : Cosmica
# @File : 1.示例
# @Project : Spider


# P74
import requests
"""
requests 和 urllib 只能支持 HTTP/1.1
对于强制使用 HTTP/2.0 的网站无能为力
"""
# 下面就是一个强制使用 HTTP/2.0 的网站
url = 'https://spa16.scrape.center/'
response = requests.get(url)
print(response.json())  # 报错
