#!/usr/bin/python3

import sqlite3
from datetime import datetime

def createDatabases(dbSQL):
    
    dbSQL.execute('''CREATE TABLE aerolineas(
        id_aerolinea INTEGER PRIMARY KEY,
        nombre_aerolinea TEXT NOT NULL)''')

    dbSQL.execute('''CREATE TABLE aeropuertos(
        id_aeropuerto INTEGER PRIMARY KEY,
        nombre_aeropuerto TEXT NOT NULL)''')

    dbSQL.execute('''CREATE TABLE movimientos(
        id_movimientos INTEGER PRIMARY KEY,
        nombre_movimiento TEXT NOT NULL)''')

    dbSQL.execute('''CREATE TABLE vuelos(
        dia DATETIME2,
        id_movimientos INTEGER,
        id_aeropuerto INTEGER,
        id_aerolinea INTEGER,
        FOREIGN KEY(id_aeropuerto) REFERENCES aeropuertos(id_aeropuerto),
        FOREIGN KEY(id_movimientos) REFERENCES movimientos(id_movimientos),
        FOREIGN KEY(id_aerolinea) REFERENCES aerolineas(id_aerolinea))''')
    

def fillDatabases(dbSQL):
    with open("datavuelos.txt") as data:
        for linea in data:
            linea = linea.split()
            dbSQL.execute("INSERT INTO vuelos(dia, id_movimientos, id_aeropuerto, id_aerolinea) VALUES(?,?,?,?)", (datetime.strptime(linea[3], '%Y-%m-%d'), int(linea[2]), int(linea[1]), int(linea[0])))

    with open("dataaeropuertos.txt") as data:
        for linea in data:
            linea = linea.split(',')
            dbSQL.execute("INSERT INTO aeropuertos(id_aeropuerto, nombre_aeropuerto) VALUES(?,?)", (int(linea[0]),linea[1]))

    with open("dataaerolineas.txt") as data:
        for linea in data:
            linea = linea.split()
            dbSQL.execute("INSERT INTO aerolineas(id_aerolinea, nombre_aerolinea) VALUES(?,?)", (int(linea[0]),linea[1]))

    with open("datamovimientos.txt") as data:
        for linea in data:
            linea = linea.split()
            dbSQL.execute("INSERT INTO movimientos(id_movimientos, nombre_movimiento) VALUES(?,?)", (int(linea[0]),linea[1]))
    
    


if __name__ == "__main__":

    databaseName = 'test.db'
    databaseConnection = sqlite3.connect(databaseName)
    dbSQL = databaseConnection.cursor()

    try:
        createDatabases(dbSQL)
        fillDatabases(dbSQL)
    except:
        print("The database is already created")

    

    databaseConnection.commit()
    databaseConnection.close()

    