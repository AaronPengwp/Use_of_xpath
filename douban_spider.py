#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron


from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}

# 1. 将目标网站上的页面抓取下来
url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'

response = requests.get(url, headers=headers)

text = response.text

# 2.将抓取下来的数据跟据一定的格式提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(ul)
# print(etree.tostring(ul[0],encoding='utf-8').decode('utf-8'))

lis = ul.xpath('./li')
movies = []
for li in lis:
    # print('8'*30)?=
    # print(etree.tostring(li, encoding='utf-8').decode('utf-8'))
    title = li.xpath('@data-title')[0]
    score = li.xpath('@data-score')[0]
    duration = li.xpath('@data-duration')[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    thumbnail = li.xpath('.//img/@src')[0]

    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'thumbnail': thumbnail
    }

    movies.append(movie)

print(movies)