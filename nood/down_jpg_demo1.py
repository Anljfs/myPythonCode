#! /usr/bin/env python
# -*- coding=utf-8 -*- 
# @Author pythontab.com
""" 
   模仿浏览器访问,从网站下载图片
"""
import re
import os
import time
import urllib
import urllib2
import random  

my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"  
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"  
]  
src_jpg_list=[]
def downpic(url,headers,name):  
    ''''' 
    @获取403禁止访问的网页 
    '''  
    try:
        randdom_header=random.choice(headers)  
  
        req=urllib2.Request(url)  
        req.add_header("User-Agent",randdom_header)  
        req.add_header("Host","mm.howkuai.com ")  
        req.add_header("Referer","http://mm.howkuai.com/")  
        req.add_header("GET",url)  
  
        content=urllib2.urlopen(req).read()
        f = open(name,"wb")
        f.write(content)
        f.close()
    except urllib2.HTTPError as e:
        print name+' failt'
    
def get_urls(url):
    html = urllib2.urlopen(url).read()
    picurl = re.compile(r'<img alt=".+?" src="(.+?)" /><br />')
    picts = picurl.findall(html)
    seq = 1
    for urls in picts:
        try:
            #time.sleep(1)
            name = re.sub(':', "_", time.ctime()[11:19])+ str(seq) +'.jpg'
            print urls
            print name
            if urls not in src_jpg_list:
                src_jpg_list.append(urls)
                downpic(urls, my_headers, '/home/dev/tu/'+name)
            else:
                print "the jpg had downloaded"
        except urllib.ContentTooShortError as e:
            print name+' failt'
            continue
        finally :
            seq+=1

def get_href(page):
    print "-----------get_href----------"
    s = urllib2.urlopen(page)
    hrefs = re.compile(r'<a href="(.+?)" target="_blank">')
    s = s.read()
    links = hrefs.findall(s)
    return links

def main():
    """for i in range(1,2):"""
    dir(urllib)
    for i in range(1,67):
        print i
        a = 'http://www.meizitu.com/a/list_1_%d.html' % i
        print a
        href = get_href(a)
        time.sleep(1)
        num = 1
        for j in href:
            print j
            get_urls(j)
            if num >1 :
                break
            num+=1
if __name__ == '__main__':
    main()
    pass
