# -*- coding: utf-8 -*-
import requests
from requests.exceptions import RequestException
import re
import json
import time


def get_page(url):
    headers={
            'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_13_3) AppleWebkit/537.36(KHTML,like\
            Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None
def parse_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime'
                       + '">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield{
                'index':item[0],
                #'image':item[1], 这个看着太麻烦了 是电影的封面
                'title':item[2],
                'actor':item[3].strip()[3:],
                'time':item[4].strip()[5:],
                'score':item[5]+item[6]}
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file(item)
if __name__=='__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)