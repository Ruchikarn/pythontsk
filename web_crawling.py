import requests

from bs4 import BeautifulSoup
from textblob import TextBlob

BASE_URL = 'https://www.onlinekhabar.com/'
content = requests.get(BASE_URL).content
print(content)

homepage = BeautifulSoup(content, "html.parser")
a_tags = homepage.find_all('a')

real_links = set()
for link in a_tags:
   # print(link)
    if '2018' in link.get('href', ''):
        real_links.add(link.get('href'))
print(real_links)

for link in real_links:
    single_news = requests.get(link).content
    singlepage = BeautifulSoup(single_news, "html.parser")
    news = singlepage.select_one('.ok18-single-post-content-wrap')
    print(news.text)
    txt_blob = TextBlob(news.text)
    print(text.blob.detect_language())
    #print(txt_blob.translate(from_lang = 'ne, to = 'en')
    print(txt_blob.statement)
