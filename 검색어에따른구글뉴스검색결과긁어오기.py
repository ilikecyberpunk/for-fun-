from bs4 import BeautifulSoup as bs
import requests

q = input("검색할 키워드를 입력하세요: ")
url = 'https://www.google.com/search?q=' + q + '&tbm=nws'

r = requests.get(url)
html_text = r.text

soup = bs(html_text, 'html.parser')
news_titles = soup.select("div.BNeawe.vvjwJb.AP7Wnd")
for i in news_titles:
    title = i.get_text()  # 텍스트 추출
    print(title)
    parent = i.find_parent('a')
    href = parent.attrs['href'] if parent else 'N/A'
    print('https://www.google.com' + href)

    