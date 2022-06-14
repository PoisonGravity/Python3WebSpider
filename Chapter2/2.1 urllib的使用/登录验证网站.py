# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 0:51
# @Author : Cosmica
# @File : 登录验证网站
# @Project : Spider
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
