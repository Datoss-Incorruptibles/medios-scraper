
import requests
from bs4 import BeautifulSoup

import csv
import json
import datetime
import time

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(today)
urlBase = "https://larepublica.pe/pf/api/v3/content/fetch/tags"
totalPages = 15
fromCount = 0
listaTotal = []
# "count":1476
with open(f'larepublica.csv', mode='w') as data:
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
        urlPage = urlBase + '?query={"from":'+ str(fromCount)+ ',"size":100,"tag":"elecciones-2021"}'

        data = requests.get(urlPage)
        jsonData = data.text
        dataFinal = json.loads(jsonData)

        arrayCards = dataFinal["content_elements"]

        for card in arrayCards:

            try:
                seccion = card["taxonomy"]["sites"][0]["path"]
            except:
                seccion = ""
            titulo = card["headlines"]["basic"]
            subtitulo = card["subheadlines"]["basic"]
            linkBase = "https://larepublica.pe"
            linkPath = card["canonical_url"]
            link= linkBase + linkPath
            image = card["promo_items"]["basic"]["url"]
            fecha = card["display_datetime"]


            print(seccion)
            print(titulo)
            print(subtitulo)
            print(link)
            print(image)
            print(fecha)
            writer.writerow([ 
                "articulo",
                seccion,
                titulo,
                subtitulo,
                link,
                image,
                fecha,
                "larepublica",
                today
                ])

        fromCount = fromCount + 100


        print(fromCount)



print("end")
