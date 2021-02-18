import requests
from bs4 import BeautifulSoup

import csv
import json
import datetime
import time

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(today)
urlBase = "https://rpp.pe/noticias/el-poder-en-tus-manos"
totalPages = 5



listaTotal = []
counter = 0
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(f'rpp.csv', mode='w') as data:
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([
          "tipo", 
          "seccion", 
          "titulo", 
          "subtitulo", 
          "url", 
          "thumbnail", 
          "fecha", 
          "medio",
          "fecha_registro"])
    for iter in range(totalPages):
        # urlPage = f'{urlBase}?page={iter+1}'
        arrayCard = []

        urlPage = f'{urlBase}?page={iter+1}'

        htmlData = requests.get(urlPage)
        s = BeautifulSoup(htmlData.text, 'lxml')
        wraper = s.find('div', attrs={'class':'row'})
        # print(wraper)
        # articles = wraper.article

        articles = wraper.findAll('article')
        # print(articles)

        for article in articles:
        # article = articles[0]
        # print(article)
            titulo = article.find('div', attrs={'class':'cont'}).h2.getText()
            subtitulo = article.find('div', attrs={'class':'cont'}).p.getText()
            link = article.find('div', attrs={'class':'cont'}).h2.a.get('href')
            imageData = article.find('figure', attrs={'class':'holder'}).a.get('data-x')
            imageJson= json.loads(imageData)
            imageRaw = imageJson["content"]
            soup = BeautifulSoup(imageRaw, 'lxml')
            image = soup.find('img').get('src')

            fecha = article.find('time', attrs={'class':'x-ago'}).getText()

            writer.writerow([ 
                "articulo",
                "",
                titulo,
                subtitulo,
                link,
                image,
                fecha,
                "rpp",
                today
                ])

print("end")
