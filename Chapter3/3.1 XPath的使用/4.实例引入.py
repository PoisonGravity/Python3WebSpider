# _*_ coding : utf-8 _*_
# @Time : 2022/6/17 13:56
# @Author : Cosmica
# @File : 4.实例引入
# @Project : Spider


from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)  # 调用 HTML 类进行初始化，这样就构造了一个 XPath 解析对象，此时它会自动修正 HTML 文本
result = etree.tostring(html)   # 输出修正后的 HTML 代码(bytes类型)
print(result.decode('utf-8'))   # 利用 decode 方法将其转为 str 类型
