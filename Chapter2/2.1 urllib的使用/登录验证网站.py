# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 0:51
# @Author : Cosmica
# @File : 登录验证网站
# @Project : Spider
# 遇到要登录的网站可能会弹出认证窗口让你输入用户名和密码登录
# 这种情况借助 HTTPBasicAuthHandler 模块就可以完成，代码如下
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
