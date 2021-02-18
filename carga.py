import json
import requests
from bs4 import BeautifulSoup
import csv

import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv('.env')

con = psycopg2.connect(database=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASS"), host=os.getenv("DB_HOST"), port="5432")
print(con)
print("Database opened successfully")






def createTable():
  cur = con.cursor()
  cur.execute('''
  DROP TABLE IF EXISTS de.medios;
  CREATE TABLE IF NOT EXISTS  de.medios (
    id serial NOT NULL,
    tipo character varying NOT NULL,
    seccion character varying NOT NULL,
    titulo character varying NOT NULL,
    subtitulo character varying NOT NULL,
    url character varying NOT NULL,
    thumbnail character varying NOT NULL,
    fecha character varying NOT NULL,
    medio character varying NOT NULL,
    fecha_registro  timestamp NOT NULL DEFAULT now(),
    fecha_modificacion timestamp NULL
    );
  ''')
  con.commit()



# ----------------------------------------------------------------

def insertTable():
  cur = con.cursor()
  with open(f'dataTotal2.json', 'r', encoding='utf-8')as outFile:
    doc = outFile.read()
    # print(doc)
    docString = json.loads(doc)

    count = 0
    # print(docString)
    cur.execute("TRUNCATE de.medios")

    for row in docString:
      if row:
        cur.execute("INSERT INTO de.medios( \
          tipo, \
          seccion, \
          titulo, \
          subtitulo, \
          url, \
          thumbnail, \
          fecha, \
          medio\
          )\
          VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (
          "articulo",
          row[0],
          row[1],
          row[2],
          row[3],
          row[4],
          row[5],
          "elcomercio"
          ))
        count+=1
        print(row)
        print("insert row ",count," success!")
        # if count == 1000 or count == 2000 or count == 3000 or count == 4000 or count == 5000 or count == 6000:
        #   con.commit()

    con.commit()
  print("Table medios cargado successfully")

  con.close()


# createTable()

# insertTable()



        # arrayCard.append(tipo)
        # arrayCard.append(titulo)
        # arrayCard.append(subtitulo)
        # arrayCard.append(linkTotal)
        # arrayCard.append(imagen)
        # arrayCard.append(fecha)


file: "https://cdn.jwplayer.com/videos/EgnYS6mP-IljTM9we.mp4" lescano
file: "https://cdn.jwplayer.com/videos/hXZXo61G-IljTM9we.mp4" acuna
file: "https://cdn.jwplayer.com/videos/bRov4HIq-IljTM9we.mp4" soto
file: "https://cdn.jwplayer.com/videos/5xNk3rM9-IljTM9we.mp4"  Alcántara
file: "https://cdn.jwplayer.com/videos/hom55GgN-IljTM9we.mp4" Arana
file: "https://cdn.jwplayer.com/videos/AT46bKdf-IljTM9we.mp4" Fujimori
file: "https://cdn.jwplayer.com/videos/qwRLFdaO-IljTM9we.mp4" Mendoza
file: "https://cdn.jwplayer.com/videos/LfHtehhi-IljTM9we.mp4" Guzmán
file: "https://cdn.jwplayer.com/videos/IID7A6On-IljTM9we.mp4" Humala
file: "https://cdn.jwplayer.com/videos/ktEt6Mj1-IljTM9we.mp4" Beingolea
file: "https://cdn.jwplayer.com/videos/0MD792JL-IljTM9we.mp4" Salaverry
file: "https://cdn.jwplayer.com/videos/hYnrFjLh-IljTM9we.mp4" Castillo
file: "https://cdn.jwplayer.com/videos/gKWLKYQI-IljTM9we.mp4" Santos
file: "https://cdn.jwplayer.com/videos/KxMCmrU3-IljTM9we.mp4" Urresti
file: "https://cdn.jwplayer.com/videos/rk1IEVWH-AoJUfW3e.mp4" Gálvez
file: "https://cdn.jwplayer.com/videos/rk1IEVWH-IljTM9we.mp4" aliaga
file: "https://cdn.jwplayer.com/videos/f9YBMdA1-IljTM9we.mp4" vega
file: "https://cdn.jwplayer.com/videos/DSsQPtBe-IljTM9we.mp4" forsyth
