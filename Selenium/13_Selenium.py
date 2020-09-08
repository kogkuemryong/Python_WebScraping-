from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키 값을 직접 입력하기 위함

browser = webdriver.Chrome() # 같은 경로에 있으면 주소를 넣지 않아도 됨.
browser.get('http://naver.com')

elem = browser.find_element_by_class_name('link_login')
# elem.click() # 로그인 누르기
# browser.back() # 이전으로
# browser.forward() # 이 앞으로
# browser.refresh() # 새로고침
# browser.back()
elem = browser.find_element_by_id('query')
# elem.send_keys('나도코딩') # 검색창에 나도 코딩 타이핑
# elem.send_keys(Keys.ENTER) # 검색 누르기

