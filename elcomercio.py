import requests
from bs4 import BeautifulSoup

import csv
import json
import datetime
import time

# from requests.adapters import HTTPAdapter
# from urllib3.util.retry import Retry

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(today)

urlBase = "https://elcomercio.pe/noticias/elecciones-2021/"
totalPages = 26


listaTotal = []
substring = "-"
# day = datetime.datetime.now()
# fechaActual = day.strftime("%x")
# fechaActual2 = datetime.datetime.strptime(fechaActual, "%m-%d-%Y").strftime("%d/%m/%Y")
counter = 0

with open(f'elcomercio.csv', mode='w') as data:
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
        urlPage = f'https://elcomercio.pe/noticias/elecciones-2021/{iter+1}'
        p12 = requests.get(urlPage)
        s = BeautifulSoup(p12.text, 'lxml')

        cards = s.findAll('div', attrs={'class':'story-item'})

        for card in cards:

            arrayCard = []
            fecha = card.find('p', attrs={'class':'story-item__date'}).getText()

            if substring not in fecha:
                fecha = today
            else:
                fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d").strftime("%d/%m/%Y")
                # print(fecha)
            seccion = card.find('a', attrs={'class':'story-item__section'}).get('href')
            titulo = card.find('a', attrs={'class':'story-item__title'}).getText()
            subtitulo = card.find('p', attrs={'class':'story-item__subtitle'}).getText()
            linkParcial = card.find('a', attrs={'class':'story-item__title'}).get('href')
            linkTotal = "https://elcomercio.pe"+linkParcial
            imagen = card.find('img', attrs={'class':'story-item__img'})['data-src']

            writer.writerow([ 
                "articulo",
                seccion,
                titulo,
                subtitulo,
                linkTotal,
                imagen,
                fecha,
                "elcomercio",
                today
                ])

            print(counter)
            print(fecha)
            counter = counter + 1

print("END")

