# _*_ coding : utf-8 _*_
# @Time : 2022/6/16 17:33
# @Author : Cosmica
# @File : 4.Client对象
# @Project : Spider


# P77 Client 对象
# 推荐的写法
# import httpx
#
# with httpx.Client() as client:
#     response = client.get('https://httpbin.org/get')
#     print(response)

# 上下两种写法是等价的，结果是一样的

# client = httpx.Client()
# try:
#     response = client.get('https://httpbin.org/get')
# finally:
#     client.close()


# 同样可以携带 headers 参数
import httpx

url = 'http://httpbin.org/headers'
headers = {'User-Agent': 'my-app/0.0.1'}
with httpx.Client(headers=headers) as client:
    r = client.get(url)
    print(r.json()['headers']['User-Agent'])


