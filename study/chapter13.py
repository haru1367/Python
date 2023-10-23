import re  # 정규 표현식을 사용하기 위한 모듈 임포트
import urllib.request  # URL에서 데이터를 가져오기 위한 모듈 임포트

# 이미지 다운로드를 위한 URL
url = 'https://images.unsplash.com/photo-1531306728370-e2ebd9d7bb99?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D'

# 이미지 다운로드 시작 메시지 출력
print('이미지 다운로드 시작')

# URL로부터 이미지 다운로드 및 'space.jpg' 파일로 저장
fname, header = urllib.request.urlretrieve(url, 'space.jpg')

# 이미지 다운로드 완료 메시지 출력
print('이미지 다운로드 완료')

# 단축 URL로부터 텍스트 데이터 가져오기
url = 'http://goo.gl/U7mSQl'
html = urllib.request.urlopen(url)
html_contents = str(html.read())

# 정규 표현식을 사용하여 데이터에서 패턴 매칭 결과를 추출하고 출력
question_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)
for result in question_results:
    print(result)

# USPTO 특허 데이터 페이지 URL
url = 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'

# URL로부터 HTML 데이터 가져오기
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('utf8'))

# 정규 표현식을 사용하여 URL 목록을 추출하고 출력
url_list = re.findall(r"(http)(.+)(zip)", html_contents)
for url in url_list:
    full_url = "".join(url)
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url, 'ipg130122.zip')
    print('다운로드 완료')

# 네이버 금융 페이지 URL
url = 'http://finance.naver.com/item/main.nhn?code=005930'

# URL로부터 HTML 데이터 가져오기
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('ms949'))

# 정규 표현식을 사용하여 주식 정보를 추출하고 출력
stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_results[0]
samsung_index = samsung_stock[1]

index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print(index[1])
