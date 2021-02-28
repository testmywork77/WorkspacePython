import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read('./configs/properties.ini')
    return config


connect_config = {
    'user': getConfig()['MYSQLDB']['user'],
    'password': getConfig()['MYSQLDB']['password'],
    'host': getConfig()['MYSQLDB']['host'],
    'database': getConfig()['MYSQLDB']['database'],
}


def getUserBaseURI():
    return getConfig()['API']['user_uri']


def getPassword():
    return "test1234"


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
