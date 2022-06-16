# _*_ coding : utf-8 _*_
# @Time : 2022/6/16 16:59
# @Author : Cosmica
# @File : sub
# @Project : Spider

# P71
# sub
import re

content = '54aK54yr5oiR54ix5L2g'
# 第一个参数传入正则表达式匹配要替换的内容，第二个参数为要替换的内容，第三个参数为原字符串
content = re.sub('\d+', '', content)
print(content)  # 得到 aKyroiRixLg，这是去除了数字的结果
