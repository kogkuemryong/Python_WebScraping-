import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# 텍스트 형태로 가져온 데이터를 lxml를 통해서 BeautifulSoup 객체로 만든 것이다.

# 네이버 웹툰 전테 목록 가져오기
cartoons = soup.find_all('a', attrs = {'class':'title'}) # 조건에 만든 모든 데이터를 찾아온다.
# class 속성이 title 인 모든 'a' 라는 element 를 반환
for cartoon in cartoons: # 타이틀의 전체를 읽어옴
    print(cartoon.get_text())


