from unicodedata import name
from winreg import QueryInfoKey
import mysql.connector
from pymongo import MongoClient

# Mysql Connection
mysql = mysql.connector.connect(
    host='localhost', password='', user='root', database='material')

mysqlCursor = mysql.cursor()

# MongoDB Connection
mongo = MongoClient('mongodb://localhost')
mongoCursor = mongo.migrasi


# Take from mongo
result = mongoCursor.id.find()

# Uraikan isi data mongo
for doc in result:
    nama = doc['name']
    description = doc['description']
    stock = str(doc['stock'])
    price = str(doc['price'])
    country = doc['country']

    query = "INSERT INTO kind_material(name, description, stock, price, country) VALUES('" + \
        nama+"', '"+description+"', "+stock+", "+price+", '"+country+"')"

    print(query)

    mysqlCursor.execute(query)
    mysql.commit()
