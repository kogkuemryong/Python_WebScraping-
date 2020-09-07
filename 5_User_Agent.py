# User-Agent 를 활용하여 제대로 스크랩핑 할 수 있도록 도와줌.

import requests
url = 'http://nadocoding.tistory.com'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

# 항상 쌍으로 사용
res = requests.get(url, headers = headers) # html을 가져옴
res.raise_for_status()

with open('nadocoding.html', 'w', encoding= 'utf-8') as f:
    f.write(res.text)

