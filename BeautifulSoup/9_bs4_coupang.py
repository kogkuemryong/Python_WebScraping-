# HTTP METHOD

# GET : 누구나 볼 수 있게 url에 적어서 사용
# https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=5&rocketAll=false&searchIndexingToken=1=4&backgroundColor=
# ? 뒤에 변수와 값으로 여러개가 들어감
# 한번에 보낼 수 있는 데이터가 정해져 있어서 많은 데이터를 보낼 수 없다.


# POST : html의 바디 영역 넣어서 사용
# 크기가 정해져 있지 않아서 많은 데이터를 사용할 수 있다.
# GET 보다 보완성이 높다.

import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

res = requests.get(url , headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
items = soup.find_all('li', attrs= {'class':re.compile('^search-product')})
# li의 'search-product'으로 시작하는 데이터를 다 가져옴
# print(items[0].find('div', attrs={'class': 'name'}).get_text())

for item in items:

    # 광고 제품은 제외
    ad_badge = item.find('span', attrs= {'class': 'ad-badge-text'})
    if ad_badge:
        print('  <광고 상품 제외합니다>')
        continue

    # 애플 제품 제외
    name = item.find('div', attrs={'class': 'name'}).get_text() # 제풍명
    if 'Apple' in name:
        print('    <Apple 상품 제외 합니다>')
        continue


    price = item.find('strong', attrs={'class' : 'price-value'}).get_text() # 가격
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find('em', attrs={'class': 'rating'})# 평점
    if rate:
        rate = rate.get_text()
    else:
        print('   <평점 없는 상품 제외합니다>')
        continue

    rate_cnt = item.find('span', attrs={'class': 'rating-total-count'})# 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 예 : (26)
        rate_cnt = rate_cnt[1:-1] # 재가공
        # print('리뷰 수 :', rate_cnt)
    else:
        print('    <평점 수 없는 상품 제외합니다>')
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)

