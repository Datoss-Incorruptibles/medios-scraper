import requests
from bs4 import BeautifulSoup

import csv
import json
import datetime
import time

# from requests.adapters import HTTPAdapter
# from urllib3.util.retry import Retry


urlBase = "https://elcomercio.pe/noticias/elecciones-2021/"
totalPages = 26
today = time.strftime("%d/%m/%Y")
print(today)


listaTotal = []
substring = "-"
# day = datetime.datetime.now()
# fechaActual = day.strftime("%x")
# fechaActual2 = datetime.datetime.strptime(fechaActual, "%m-%d-%Y").strftime("%d/%m/%Y")
today = time.strftime("%d/%m/%Y")

counter = 0
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
        tipo = card.find('a', attrs={'class':'story-item__section'}).get('href')
        titulo = card.find('a', attrs={'class':'story-item__title'}).getText()
        subtitulo = card.find('p', attrs={'class':'story-item__subtitle'}).getText()
        linkParcial = card.find('a', attrs={'class':'story-item__title'}).get('href')
        linkTotal = "https://elcomercio.pe"+linkParcial
        imagen = card.find('img', attrs={'class':'story-item__img'})['data-src']

        arrayCard.append(tipo)
        arrayCard.append(titulo)
        arrayCard.append(subtitulo)
        arrayCard.append(linkTotal)
        arrayCard.append(imagen)
        arrayCard.append(fecha)

        listaTotal.append(arrayCard)
        # print(tipo)
        # print(titulo)
        print(counter)
        print(fecha)
        counter = counter + 1
        # print(subtitulo)
        # print(imagen)

dataFinalJson = json.dumps(listaTotal)
with open('dataTotal2.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)
