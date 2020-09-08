'''
[헤드라인 뉴스]
1. 무슨 무슨 일이...
 (링크 : http://...)
2. 무슨 무슨 일이...
 (링크 : http://...)
3. 무슨 무슨 일이...
 (링크 : http://...)
'''
import requests
from bs4 import BeautifulSoup

def creat_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def scrape_headline_news():
    print('[헤드라인 뉴스]')
    url = 'https://news.naver.com'
    soup = creat_soup(url)

    news_list = soup.find('ul', attrs={'class':'hdline_article_list'}).find_all('li', limit=3) # limit=3 : 3개 까지만 찾음.
    for index, news in enumerate(news_list): # 출력할 때 인덱스를 출력하기 위해서 enumerate 사용
        title = news.find('a').get_text().strip()
        link = url + news.find('a')['href']
        print("{}. {}".format(index+1 , title))
        print('  (링크 : {})'.format(link))
    print()

if __name__=='__main__':
    scrape_headline_news()