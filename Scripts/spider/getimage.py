#-*- coding=utf-8 -*-
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getaddr(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    t = 0
    for l in imglist:
        urllib.urlretrieve(l, 'C:\Users\JoJo\Python\Scripts\spider\pic\%s.jpg' % t)
	t += 1

html = getHtml("http://tieba.baidu.com/p/4120094087")

getaddr(html)
