#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron


from lxml import etree
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36',
    'Referer': 'https://www.dytt8.net/'
}

URL_BASE = 'https://www.dytt8.net/'


# 1. 将目标网站上的页面抓取下来
def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath('//table[@class="tbspan"]//a/@href')
    detail_urls = map(lambda url: URL_BASE + url, detail_urls)

    return detail_urls


def parse_detail_page(url):
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)

    movie = {}
    title = html.xpath('//div[@class="title_all"]//font//text()')[0]
    # print(title)
    movie['title'] = title
    zoomE = html.xpath('//div[@id="Zoom"]')[0]
    imgs = zoomE.xpath('.//img/@src')
    # 电影海报
    cover = imgs[0]
    # 电影截图
    screenshot = imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    # print(movie)

    def pares_info(info, rule):
        return info.replace(rule, "").strip()

    infos = zoomE.xpath('.//text()')
    for index, info in enumerate(infos):
        # print(info)
        # print(index)
        # print(type(infos),type(info))
        # print('&'*30)
        if info.startswith("◎年　　代"):
            info = pares_info(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = pares_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = pares_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = pares_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = pares_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = pares_info(info, "◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = pares_info(info, "◎主　　演")
            actors = [info]
            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎简　　介"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = pares_info(info, "◎简　　介")
            profiles = []
            for x in range(index + 1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
                profiles.append(profile)
                movie['profiles'] = profiles
                print(profiles, type(profiles), movie["profiles"])

    download_url = html.xpath('//td[@bgcolor="#fdfddf"]/a/@href')[0]
    movie['download_url'] = download_url
    return movie


def spider():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    # 用来控制总共有7页
    for x in range(1, 8):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        # 用来遍历一页中的所有电影的主详情url
        for detail_url in detail_urls:
            # print(detail_url)
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movies)
        #     break
        # break


if __name__ == '__main__':
    spider()
