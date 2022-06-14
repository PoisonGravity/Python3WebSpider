# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 0:02
# @Author : Cosmica
# @File : request
# @Project : Spider
from urllib import request, parse

url = 'https://www.httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'www.httpbin.org'
}
dict = {'name': 'germey'}
# 将字典类型的数据转为 bytes 类型
data = bytes(parse.urlencode(dict), encoding='utf-8')
# 第二个数据 data 如果要传数据，则必须是 bytes 类型的
req = request.Request(url=url, data=data, headers=headers, method='POST')
# 我们依然使用 urlopen 方法来发送请求,只不过参数不再是 URL,而是一个 Request 类型的对象
response = request.urlopen(req)
print(response.read().decode('utf-8'))


