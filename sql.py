#!/usr/bin/python3

import sqlite3

from rx import catch

def createDatabases(database):
    
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
        dia DATE PRIMARY KEY,
        id_movimientos INTEGER,
        id_aeropuerto INTEGER,
        id_aerolinea INTEGER,
        FOREIGN KEY(id_aeropuerto) REFERENCES aeropuertos(id_aeropuerto),
        FOREIGN KEY(id_movimientos) REFERENCES movimientos(id_movimientos),
        FOREIGN KEY(id_aerolinea) REFERENCES aerolineas(id_aerolinea))''')
    


    
    
    


if __name__ == "__main__":

    databaseName = 'test.db'
    databaseConnection = sqlite3.connect(databaseName)
    dbSQL = databaseConnection.cursor()

    try:
        createDatabases(dbSQL)
    except:
        print("The database is already created")

    databaseConnection.commit()
    databaseConnection.close()

    