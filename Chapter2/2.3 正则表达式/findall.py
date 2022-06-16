# _*_ coding : utf-8 _*_
# @Time : 2022/6/15 23:56
# @Author : Cosmica
# @File : findall
# @Project : Spider


# P71
# findall 获取与正则表达式相匹配的所有字符串
import re
html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
#
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)  # 所有匹配到的结果
print(type(results))    # 列表类型
for result in results:
    print(result)   # 列表中每个元素都是元组类型的
    print(result[0], result[1], result[2])  # 用索引取出每个条目即可

# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# for result in results:
#     print(result[1])
#
# html = re.sub('<a.*?>|</a>', '', html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())



