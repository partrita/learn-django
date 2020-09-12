from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Headline
# import urllib3
# urllib3.disable_warnings()


def scrape(request):
    session = requests.Session()
    session.headers = {
        "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://news.naver.com/"
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    News = soup.find_all('div', {'class': 'hdline_article_tit'})
    for article in News:
        main = article.find('a')
        link = main['href']
        # image_src = str(main.find('img')['srcset']).split(" ")[-4]
        title = main.text
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = 'https://news.naver.com/'+link
        # new_headline.image = image_src
        try:
            new_headline.save()
        except:
            print('이미 불러온 뉴스입니다.')
    return redirect("../")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context)
