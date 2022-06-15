# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 14:41
# @Author : Cosmica
# @File : cookie
# @Project : Spider
# P36
# 获取网站的 Cookie
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
# 分别输出每个 Cookie 条目的名称和值
for item in cookie:
    print(item.name + "=" + item.value)
