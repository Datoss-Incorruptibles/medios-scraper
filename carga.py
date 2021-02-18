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
  # with open('rpp.csv', 'r') as f:
  with open('larepublica.csv', 'r') as f:

      cur.copy_expert(sql=copy_sql, file=f)
      con.commit()
      con.close()
  print("Table medios cargado successfully")

  con.close()


# createTable()
cargaCSVtoDB()






