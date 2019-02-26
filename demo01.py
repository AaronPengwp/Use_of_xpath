#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron

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
#
# htmlElement = etree.HTML(text)
#
# print(htmlElement)
# print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

parser = etree.HTMLParser(encoding='utf-8')
htmlElement = etree.parse("lagou.html", parser=parser)
print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

