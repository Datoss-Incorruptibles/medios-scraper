import requests
from bs4 import BeautifulSoup

import csv
import json
import datetime
import time
import re


today = time.strftime("%d/%m/%Y")
name = "PORFIRIO VARGAS QUISPE"
urlBase = "https://news.google.com/rss/search"
counter = 0

with open(f'candidatosv3.csv', mode='w') as data:
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([
          "fullname", 
          "jne_idhojavida", 
          "documento_identidad", 
          "title", 
          "link",
          "pubdate", 
          "source_medio", 
          "source_link",
        #   "imgLink"
          "fecha_registro"])

    with open('candi.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
  
            print(row[0])
            urlPage = f'{urlBase}?q={row[0]}&hl=es-419&gl=PE&ceid=PE%3Aes-419'
            # print(urlPage)
            p12 = requests.get(urlPage)
            s = BeautifulSoup(p12.text, 'lxml')

            cards = s.findAll('item')
            for card in cards:
                complete_string = str(card)
                title =  card.find('title').getText()
                link = re.search('<link/>(?s)(.*)<guid',complete_string).group(1)
                pubdate = card.find('pubdate').getText()
                sourceMedio = card.find('source').getText()
                sourceLink = card.find('source').get('url')

                # try:
                #     p12 = requests.get(link)
                #     s = BeautifulSoup(p12.text, 'lxml')
                #     imgTag= s.find('meta', attrs={'property':'og:image'})
                #     imgLink = imgTag.get('content')
                #     if  "http"  not in imgLink:
                #         imgLink = f'https:{imgLink}'
                #     print(imgLink)
                # except:
                #     imgLink = "vacio"
                #     print(imgLink)

                # print(title)
                # print(link)
                # print(pubdate)
                # print(source)
                # print(sourceLink)
                # print(imgLink)

                writer.writerow([ 
                row[0],
                row[1],
                row[2],
                title,
                link,
                pubdate,
                sourceMedio,
                sourceLink,
                # imgLink,
                today
                ])
            counter = counter + 1 
            print(counter)
        