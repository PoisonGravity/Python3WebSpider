# _*_ coding : utf-8 _*_
# @Time : 2022/6/14 23:15
# @Author : Cosmica
# @File : urlopen方法中传递data参数
# @Project : Spider
import urllib.parse
import urllib.request
# bytes方法中第一个参数得是str(字符串)类型,因此先将字典转字符串,第二个参数指定编码格式，这里指定为 utf-8
data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
# 在urlopen方法中传递data参数时，需要利用bytes方法将参数转为字节流编码格式的内容
response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
