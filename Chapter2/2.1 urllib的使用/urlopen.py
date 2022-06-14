# _*_ coding : utf-8 _*_
# @Time : 2022/6/14 23:01
# @Author : Cosmica
# @File : urlopen
# @Project : Spider
import urllib.request

response = urllib.request.urlopen('https://www.python.org')
# 打印python官网的源码
print(response.read().decode('utf-8'))
# 利用type方法输出响应的类型
print('响应的类型：', end="")
print(type(response))
# 调用其中的方法、属性打印信息
print('状态码：', end="")
print(response.status)
print('响应头信息：', end="")
print(response.getheaders())
print('获取响应头中Server的值：', end="")
print(response.getheader('Server'))

