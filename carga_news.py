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
  DROP TABLE IF EXISTS de.medios_google;
  CREATE TABLE IF NOT EXISTS  de.medios_google (
    fullname character varying  NULL,
    jne_idhojavida character varying  NULL,
    documento_identidad character varying  NULL,
    title character varying  NULL,
    link character varying  NULL,
    pubdate character varying  NULL,
    source_medio character varying  NULL,
    source_link character varying  NULL,
    fecha_registro  timestamp NOT NULL DEFAULT now()
    );
  ''')
  con.commit()



# ----------------------------------------------------------------

def cargaCSVtoDB():
  cur = con.cursor()

  copy_sql = """
            COPY de.medios_google FROM stdin WITH CSV HEADER
            DELIMITER as ','
            """

  # with open('elcomercio.csv', 'r') as f:
  # with open('rpp.csv', 'r') as f:
  with open('candidatosv3.csv', 'r') as f:

      cur.copy_expert(sql=copy_sql, file=f)
      con.commit()
      con.close()
  print("Table medios cargado successfully")

  con.close()


createTable()
cargaCSVtoDB()






