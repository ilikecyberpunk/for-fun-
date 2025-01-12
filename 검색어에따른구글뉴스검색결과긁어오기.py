# from bs4 import BeautifulSoup as bs
# import requests

# q = input("검색할 키워드를 입력하세요: ")
# url = 'https://www.google.com/search?q=' + q + '&tbm=nws'

# r = requests.get(url)
# html_text = r.text

# soup = bs(html_text, 'html.parser')
# news_titles = soup.select("div.BNeawe.vvjwJb.AP7Wnd")
# for i in news_titles:
#     title = i.get_text()  # 텍스트 추출
#     print(title)
#     parent = i.find_parent('a')
#     href = parent.attrs['href'] if parent else 'N/A'
#     print('https://www.google.com' + href)

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests


bg_color = 'black'
fg_color = 'lime'
font_large = ('Helvetica', 16)

window = tk.Tk()
window.title("뉴스 검색기")
window.geometry('900x600')
window.configure(bg=bg_color)

rafio_var = tk.StringVar(value="Google News")

radio1 = tk.Radiobutton(window, text="Google News", variable=rafio_var, value="Google News", bg=bg_color, fg=fg_color, selectcolor=bg_color, font=font_large)
radio1.grid(row=0, column=0, padx=20, pady=10, sticky='w')
radio2 = tk.Radiobutton(window, text="Naver News", variable=rafio_var, value="Naver News", bg=bg_color, fg=fg_color, selectcolor=bg_color, font=font_large)
radio2.grid(row=0, column=1, padx=20, pady=10, sticky='w')

a = tk.Label(window, text="관심있는 뉴스 키워드 입력 ", bg=bg_color, fg=fg_color, font=font_large)
a.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky='w')
a1 = tk.Entry(window, bg=bg_color, fg=fg_color, insertbackground=fg_color, font=font_large)
a1.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky='w')

b1 = tk.Label(window, text='', bg=bg_color, fg=fg_color, font=font_large, justify='left')
b1.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky='w')

def search():
    if rafio_var.get() == "Naver News":
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + '%s' % a1.get()
        r = requests.get(url)
        html_text = r.text

        current_text = b1.cget("text")
        new_text = ''

        soup = bs(r.text, 'html.parser')
        news_titles = soup.select("a.news_tit")
        for i in news_titles:
            title = i.get_text()
            href = i.attrs['href']
            new_text += f"{title} \n {href} \n\n"

        b1.config(text=current_text + new_text)

    elif rafio_var.get() == "Google News":
        url = 'https://www.google.com/search?q=' + a1.get() + '&tbm=nws'
        r = requests.get(url)
        html_text = r.text

        current_text2 = b1.cget("text")
        new_text2 = ''

        soup = bs(html_text, 'html.parser')
        news_titles = soup.select("div.BNeawe.vvjwJb.AP7Wnd")
        for i in news_titles:
            title = i.get_text()
            parent = i.find_parent('a')
            href = parent.attrs['href']
            new_text2 += f"{title}\n https://www.google.com{href} \n\n"
        b1.config(text=current_text2 + new_text2)

def d():
    b1.config(text='')

a2 = tk.Button(window, text="검색 !!", command=search, bg=bg_color, fg=fg_color, font=font_large)
a2.grid(row=3, column=0, padx=20, pady=10, sticky='w')
b3 = tk.Button(window, text="삭제 !!", command=d, bg=bg_color, fg=fg_color, font=font_large)
b3.grid(row=3, column=1, padx=20, pady=10, sticky='w')

window.mainloop()