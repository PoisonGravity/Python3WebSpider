# _*_ coding : utf-8 _*_
# @Time : 2022/6/16 17:21
# @Author : Cosmica
# @File : 3.基本使用
# @Project : Spider


# P75 httpx 的基本使用
# import httpx
#
# response = httpx.get('https://httpbin.org/get')
# print(response.status_code)
# print(response.headers)
# print(response.text)


# 下面换一个 User-Agent 再请求一次
import httpx

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
response = httpx.get('https://httpbin.org/get', headers=headers)

print(response.text)
