# _*_ coding : utf-8 _*_
# @Time : 2022/6/16 17:21
# @Author : Cosmica
# @File : 3.基本使用
# @Project : Spider


# P75
import httpx

response = httpx.get('https://httpbin.org/get')
print(response.status_code)
print(response.headers)
print(response.text)


