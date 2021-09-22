import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis(hotel_id text PRIMARY KEY,\
     nome text, estrelas real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES('alpha', 'Hotel Alpha', 5, 390.60, 'Vitoria')"

cursor.execute(cria_tabela)
cursor.execute(cria_tabela)

connection.commit()
connection.close()