'''
[오늘의 날씨]
흐림 , 어제 보다 00 높아요
현재 00ºC (최저 00º / 최고 00º)
오전 강수량 00% / 오후 강수량 00%

미세먼지  00㎍/㎥  좋음
초미세먼지  00㎍/㎥  좋음

'''
import requests
from bs4 import BeautifulSoup


def scrape_weather():
    print('[오늘의 날씨]')
    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # 흐림 , 어제 보다 00 높아요
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()

    # 현재 00ºC (최저 00º / 최고 00º)
    Curr_temp = soup.find('p', attrs= {'class':'info_temperature'}).get_text().replace('도씨', '') # 현재온도
    min_temp = soup.find('span', attrs = {'class':'min'}).get_text() # 최저온도
    max_temp = soup.find('span', attrs = {'class':'max'}).get_text() # 최고온도

    # 오전 강수량 00% / 오후 강수량 00%
    morning_rain_rate = soup.find('span', attrs={'class':'point_time morning'}).get_text().strip() # strip() 공백 제거 : 오전 강수 확률
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수 확률


    # 미세먼지  00㎍/㎥  좋음
    # 초미세먼지  00㎍/㎥  좋음
    dust = soup.find('dl' , attrs={'class':'indicator'})
    pm10 = dust.find_all('dd')[0].get_text()
    pm25 = dust.find_all('dd')[1].get_text()

    # 출력
    print(cast)
    print('현제 {} (최저 {} / 최고 {})'.format(Curr_temp, min_temp, max_temp))
    print('오전 {} / 오후 {}'.format(morning_rain_rate, afternoon_rain_rate))
    print()
    print('미세먼지 {}'.format(pm10))
    print('초미세먼지 {}'.format(pm25))


if __name__=='__main__':
    scrape_weather()# 오늘의 날씨 정보 가져오기
