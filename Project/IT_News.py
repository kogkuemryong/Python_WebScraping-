'''
[IT 뉴스]
1. 무슨 무슨 일이...
 (링크 : http://...)
2. 무슨 무슨 일이...
 (링크 : http://...)
3. 무슨 무슨 일이...
 (링크 : http://...)
'''

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
def create_soup(url):
    res = requests.get(url, headers= headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return  soup

def scrape_IT_News():
    print('[IT 뉴스]')
    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = create_soup(url)

    it_news = soup.find('ul', attrs={'class', "type06_headline"}).find_all('li', limit=3)
    for index, news in enumerate(it_news):
        a_idx = 0
        img = news.find('img')
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그 정보를 사용

        a_tag = news.find_all('a')[a_idx]
        title = a_tag.get_text().strip() # 원하는 인덱스를 가져오게 만듬
        link = a_tag['href']

        print('{}. {}'.format(index+1, title))
        print('  (링크 : {})'.format(link))
    print()


if __name__ =='__main__':
    scrape_IT_News()





