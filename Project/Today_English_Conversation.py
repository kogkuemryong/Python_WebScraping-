'''
[오늘의 영어 회화]
(영어 지문)
Jason : Hi....?
Kim : Hi...

(한글 지문)
Jason : 안녕...?
Kim : 안녕...
'''

import requests
from bs4 import BeautifulSoup
import re

def scrape_english():
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text , 'lxml')

    print('[오늘의 영어 회화]')

    sentences = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})
    print('(영어 지문)')
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정, 5 ~ 8까지 잘라서 가져옴 // 인 이유는 7과 같이 소수점이 나오는 것을 방지하여 몫만 가져옴
        print(sentence.get_text().strip())

    print()
    print('(한글 지문)')
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

    print()


if __name__== '__main__':
    scrape_english()