import requests
from bs4 import BeautifulSoup

url ='https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url) # url 를 읽음
res.raise_for_status() # 문제가 생기면 프로그램 종료를 시켜줌

soup = BeautifulSoup(res.text, 'lxml') # 텍스트 형태로 가져온 데이터를 lxml를 통해서
                                       # BeautifulSoup 객체로 만든 것이다.

'''
해당 웹페이지를 잘 알 때 사용

print(soup.title) # <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text()) # 글자만 빼옴 / 네이버 만화 > 요일별  웹툰 > 전체웹툰
print(soup.a) # soup 전체에서 첫번째 a element 출력
print(soup.a.attrs) # a element의 속성 정보를 출력
print(soup.a['href']) # a element의 href 속성 '값' 정보를 출력`
'''

# print(soup.find('a', attrs={'class' :'Nbtn_upload'})) # class = 'Nbtn_upload' 인 a element를 찾아줘
# print(soup.find(attrs={'class' :'Nbtn_upload'})) # class = 'Nbtn_upload'인 어떤 element 를 찾아줘

# print(soup.find('li', attrs={'class':'rank01'}))

# rank1 = soup.find('li', attrs={'class':'rank01'})
# print(rank1.a.get_text()) # 글자만
# print (rank1.next_sibling) # 아무것도 출력 안됨
# rank2 = rank1.next_sibling.next_sibling # 형제 관계로 넘어가게 해준다.
# rank3 = rank2.next_sibling.next_sibling
# rank4 = rank3.next_sibling.next_sibling
# print(rank4.get_text())

# rank2 = rank3.previous_sibling.previous_sibling # 이전으로 가기
# print(rank1.parent) # 부모로 가기

# rank2 = rank1.find_next_sibling('li')
# print(rank2.a.get_text()) # next.sibling 을 여러번 사용하게 될 때 대신하여 유용하게 사용.
#
# rank3 = rank2.find_next_sibling('li')
# print(rank3.a.get_text())
#
# rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())
# print (rank1.find_next_siblings('li'))

webtooon = soup.find('a' , text = '인생존망-43화 : 너 뽀뽀하려고 그랬지!!!')
print(webtooon)



