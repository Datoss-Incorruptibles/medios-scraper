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
    tipo character varying  NULL,
    seccion character varying  NULL,
    titulo character varying  NULL,
    subtitulo character varying  NULL,
    url character varying  NULL,
    thumbnail character varying  NULL,
    fecha character varying  NULL,
    medio character varying  NULL,
    fecha_registro  timestamp NOT NULL DEFAULT now()
    );
  ''')
  con.commit()



# ----------------------------------------------------------------

def cargaCSVtoDB():
  cur = con.cursor()

  copy_sql = """
            COPY de.medios FROM stdin WITH CSV HEADER
            DELIMITER as ','
            """

  # with open('elcomercio.csv', 'r') as f:
  with open('rpp.csv', 'r') as f:

      cur.copy_expert(sql=copy_sql, file=f)
      con.commit()
      con.close()
  print("Table medios cargado successfully")

  con.close()


# createTable()
cargaCSVtoDB()





# file: "https://cdn.jwplayer.com/videos/EgnYS6mP-IljTM9we.mp4" lescano
# file: "https://cdn.jwplayer.com/videos/hXZXo61G-IljTM9we.mp4" acuna
# file: "https://cdn.jwplayer.com/videos/bRov4HIq-IljTM9we.mp4" soto
# file: "https://cdn.jwplayer.com/videos/5xNk3rM9-IljTM9we.mp4"  Alcántara
# file: "https://cdn.jwplayer.com/videos/hom55GgN-IljTM9we.mp4" Arana
# file: "https://cdn.jwplayer.com/videos/AT46bKdf-IljTM9we.mp4" Fujimori
# file: "https://cdn.jwplayer.com/videos/qwRLFdaO-IljTM9we.mp4" Mendoza
# file: "https://cdn.jwplayer.com/videos/LfHtehhi-IljTM9we.mp4" Guzmán
# file: "https://cdn.jwplayer.com/videos/IID7A6On-IljTM9we.mp4" Humala
# file: "https://cdn.jwplayer.com/videos/ktEt6Mj1-IljTM9we.mp4" Beingolea
# file: "https://cdn.jwplayer.com/videos/0MD792JL-IljTM9we.mp4" Salaverry
# file: "https://cdn.jwplayer.com/videos/hYnrFjLh-IljTM9we.mp4" Castillo
# file: "https://cdn.jwplayer.com/videos/gKWLKYQI-IljTM9we.mp4" Santos
# file: "https://cdn.jwplayer.com/videos/KxMCmrU3-IljTM9we.mp4" Urresti
# file: "https://cdn.jwplayer.com/videos/rk1IEVWH-AoJUfW3e.mp4" Gálvez
# file: "https://cdn.jwplayer.com/videos/rk1IEVWH-IljTM9we.mp4" aliaga
# file: "https://cdn.jwplayer.com/videos/f9YBMdA1-IljTM9we.mp4" vega
# file: "https://cdn.jwplayer.com/videos/DSsQPtBe-IljTM9we.mp4" forsyth
