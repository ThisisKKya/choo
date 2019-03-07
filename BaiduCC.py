#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      清墨鱼
#
# Created:     01/02/2019
# Copyright:   (c) 清墨鱼 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self,site):
        self.site=site

    def scrape(self):
        r=urllib.request.urlopen(self.site)
        html=r.read()
        parser="html.parser"
        sp=BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url=tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n"+url)

a = "https://news.baidu.com/"

Scraper(a).scrape()
