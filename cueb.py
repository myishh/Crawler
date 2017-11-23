# -*-coding:utf-8 -*-
# This is a simple web crawler, which is designed to collect java or <br>python developer job positions in the site jy.cueb.edu.cn 

__author__  =   "myishh"
__email__   =   "myishh[at]qq.com"

import requests
import time
from bs4 import BeautifulSoup

def trade_spider(max_page):
    f = open("cueb.md", "w")
    page = 1
    while page <= max_page:
        url = "http://jy.cueb.edu.cn/front/channel.jspa?channelId=764&parentId=764&curPage=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.find_all('a', {'id':'a_prop_'}):
            title = link.string.strip()
            #print(title)
            href =  "http://jy.cueb.edu.cn" + link.get("href")
            #print(href)
            #print("")
            #print(link.get("title"))
            get_single_item_info(href, f, page)
        page += 1
    f.close()

def get_single_item_info(item_url, f, page):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for item in soup.find_all("span"):
        content = item.string
        if isinstance(content, str):
            if ("java" in content.lower()
                or "python" in content.lower()
                #or u'\u6570\u636E\u6316\u6398' in content.lower()
                ):
                print_company_info(soup, item_url, f, page)
                break
                #print(isinstance(title.string, str))
                #print(type(title))
                #print(title)
                #print("Company Name: \t" + title)

def print_company_info(soup, url, f, page):
    for item in soup.find_all("span", {"class":"pd10 w230"}):
        print(item.string + " page(" + (str(page) + ")"))
        f.write(item.string + "</br>")
        break
    print(url + "\n")
    f.write(url + "</br>" + "</br>")

cnt = int(input("Input an int to decide crwal how many pages: "))
trade_spider(cnt)
