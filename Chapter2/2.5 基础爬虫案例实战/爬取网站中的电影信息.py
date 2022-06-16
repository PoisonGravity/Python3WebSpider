# _*_ coding : utf-8 _*_
# @Time : 2022/6/16 18:53
# @Author : Cosmica
# @File : 爬取网站中的电影信息
# @Project : Spider


# P82
# 目标网站：https://ssr1.scrape.center/
'''
本节目标：
    利用 requests 爬取这个站点每一页的电影列表，顺着列表再爬取每个电影的详情页
    利用正则表达式提取每部分电影的名称、封面、类别、上映时间、评分、剧情简介等内容
    把以上爬取的内容保存为 JSON 文本文件
    使用多进程实现爬取加速
'''

# 定义基础变量并且引入一些必要的库
import requests  # 用于爬取页面
import logging  # 用于输出信息
import re   # 实现正则表达式解析
from urllib.parse import urljoin    # URL 拼接

#  定义日志输出级别和格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://ssr1.scrape.center'    # 当前站点的根 URL
TOTAL_PAGE = 10  # 需要爬取的总页码数


def scrape_page(url):
    """
    定义一个通用的爬取页面的方法
    :param url: 需要爬取的网站 url
    :return: 目标网页的 HTML 代码
    """
    logging.info('scraping %s...', url)  # 打印日志信息
    try:
        response = requests.get(url)
        if response.status_code == 200:  # 如果状态码为200则返回页面源码
            return response.text
        # 否则输出错误信息
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    # 捕获爬取异常，输出对应错误信息
    except requests.RequestException:
        # exc_info 参数设置为 True，可以打印 Traceback 错误堆栈信息
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    """
    列表页的爬取
    :param page: 列表页的页码
    :return: 列表页的 HTML 代码
    """
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    """
    解析列表页
    :param html: 列表页的 HTML 代码
    :return: 列表页中每个电影详情页的 URL
    """
    # 构造正则表达式对象，用于提取标题超链接 href 属性
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)   # 根据正则表达式在 html 代码中匹配符合的字符串
    if not items:   # 如果 items 为空，直接返回空列表即可
        return []
    for item in items:  # 不为空，则遍历处理即可
        detail_url = urljoin(BASE_URL, item)    # 拼接 URL
        logging.info('get detail url %s', detail_url)
        yield detail_url    # 调用 yield 返回即可


def scrape_detail(url):
    """
    爬取详情页
    :param url: 详情页的 URL
    :return: 详情页的 HTML 代码
    """
    return scrape_page(url)


def parse_detail(html):
    """
    接收电影详情页的 HTML 代码并解析提取其中数据
    :param html: 电影详情页的 HTML 代码
    :return: 以字典的形式返回电影详细信息
    """
    cover_pattern = re.compile(
        'class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile(
        '<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)

    cover = re.search(cover_pattern, html).group(
        1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(
        1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(
        categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(
        1) if re.search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(
        1).strip() if re.search(drama_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1).strip()
                  ) if re.search(score_pattern, html) else None

    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }


def main():
    # page 的范围：1-10
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        logging.info('detail urls %s', list(detail_urls))


# main 方法
if __name__ == '__main__':
    main()
