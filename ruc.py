# -*- coding:utf-8 -*-
# This is a web crawler, which is used to collect job positions of java or python developer in the site of <br>rdjy.ruc.edu.cn(Renmin Univ of China)

__author__  =   "myishh"
__email__   =   "myishh[at]qq.com"

import requests
import time
from bs4 import BeautifulSoup

def trade_spider(max_page):
    f = open("ruc.md", "w")
    page = 1
    while page <= max_page:
        url = "http://rdjy.ruc.edu.cn/cms/employment/?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        soup2 = soup.find("div", {"class":"list"})
        for link in soup2.find_all('a'):
            href =  "http://rdjy.ruc.edu.cn" + link.get("href")
            #print(href)
            get_single_company_info(href, f, page)
        page += 1
    f.close()

def get_single_company_info(item_url, f, page):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    soup2 = soup.find("div", {"class":"col-md-10 article "})
    #print(type(soup2))
    for item in soup2.find_all("span"):
        content = item.string
        if isinstance(content, str):
            if ("java" in content.lower()
                or "python" in content.lower()
                #or u'\u6570\u636E\u6316\u6398' in content.lower()
                ):
                print_company_info(soup2, item_url, f, page)
                break

def print_company_info(soup2, url, f, page):
    item =  soup2.find("h3")

    #right here, if use 'item.string', the result will be 'none'!!
    #remember 'item.string' only can be used in the smallest tag!!
    print(item.text + " page(" + (str(page) + ")"))
    f.write(item.text + "</br>")
    print(url + "\n")
    f.write(url + "</br>" + "</br>")

#cnt = int(input("Input an int to decide crwal how many pages: "))
cnt = 30
trade_spider(cnt)
