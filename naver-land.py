import requests
from bs4 import BeautifulSoup
import json
import re
from itertools import count
from time import sleep
import csv



# 1. 네이버 부동산에 접속한다.
def connect():
    url_naver_land = 'http://land.naver.com/'
    r = requests.get(url_naver_land)
    r.encoding = "utf-8"
    html = r.text
    print(html)

# 2. '관악구'로 검색한다.

def kwanak():
    url_kwanak = 'http://land.naver.com/search/search.nhn?query=%EA%B4%80%EC%95%85%EA%B5%AC'
    r = requests.get(url_kwanak)
    r.encoding = "utf-8"
    html = r.text
    print(html)


# 3. 매물 정보를 가져온다.
def forsale():
    params = {
    'query':'관악구',
    'regionCode':1162000000,
    'regionType':'region2',
    'sortOption':'undefined',
    'isFirstSiteArticle':'true',
    'isComplexRegion':'false',
    'isSpotSearch':'false',
    'spotList':'undefined',
    'page':3}

    url_forsale = 'http://land.naver.com/search/articleSearch.nhn'
    r = requests.get(url_forsale, params=params)
    r.encoding = 'utf-8'
    r = r.text
    r_dict = json.loads(r)

    if r_dict['articleInfo']['cfmArticleList']:
        r_list = r_dict['articleInfo']['cfmArticleList']
        forsale_num = len(r_list)

        for i in range(forsale_num):
            trade_type = r_list[i]['tradeTypeCodeName']
            article_type = r_list[i]['articleTypeCodeName']
            article_name = r_list[i]['articleName']
            sizeDesc = r_dict[i]['sizeDesc']
            floor = r_dict[i]['floor']
            priceShort = r_dict[i]['priceShort']
            realterName = r_dict[i]['realterName']

            with open('naver-land-'+ params['query'] +'.csv', 'a', newline='') as f:
                r_writer = csv.writer(f)
                r_writer.writerow([trade_type, article_type, article_name, sizeDesc, floor, priceShort, realterName])

    # else:
    #     print("더 이상 자료 없음")
    #     break

forsale()
