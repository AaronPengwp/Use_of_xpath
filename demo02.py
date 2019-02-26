#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron

from lxml import etree
import json

# 1.获取所有tr标签

pares = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html", parser=pares)
trs = html.xpath("//tr")

# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 2.获取第２个tr标签
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))


# 3.获取所有class等于even的tr标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
# 4.获取所有a标签的href属性
# asList = html.xpath("//a[@href]") #错误写法,获取的是属性的内容
# asList = html.xpath("//a/@href")
# for a in asList:
#     print("https://hr.tencent.com/"+a)
# 5.获取所有职位信息(纯文本)
trs = html.xpath("//tr[position()>1]")
# print(etree.tostring(html.xpath("//tr[@class!='f']")[1],encoding='utf-8').decode('utf-8'))
print(len(trs))
del (trs[-1])
print(len(trs))
positions = []
for tr in trs:
    # href = tr.xpath("//a") #这种写法会忽视tr,相当于html.xpath的写法了
    # 在某个标签下，再执行xpath函数，获取这个标签下的子孙元素
    # 　那么应该在//之前加一个点，代表在当前元素下获取
    href = tr.xpath(".//a/@href")[0]
    fullurl = "https://hr.tencent.com/" + href
    # title = tr.xpath("./td[1]//text()")[0]
    title = tr.xpath("./td[1]/a/text()")[0]
    category = tr.xpath("./td[2]/text()")[0]
    # print(type(category))
    # print(category)
    nums = tr.xpath("./td[3]/text()")[0]
    address = tr.xpath("./td[4]/text()")[0]
    pubtime = tr.xpath("./td[5]/text()")[0]

    position = {
        'url': fullurl,
        'title': title,
        'category': category,
        'nums': nums,
        'address': address,
        'pubtime': pubtime
    }

    positions.append(position)

# print(positions)
with open("positions.txt", 'w', encoding='utf-8') as fs:
        json.dump(positions, fs)

with open("positions.txt", 'r', encoding='utf-8') as fs:

       dics = json.load(fs, strict=False)
       print(dics)
       # dics = fs.read()
       # print(type(dics))
       # print(dics)
