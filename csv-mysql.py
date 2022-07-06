import csv
import mysql.connector
from pymongo import MongoClient

# Mysql Connection
mysql = mysql.connector.connect(
    host='localhost', password='', user='root', database='csv_mysql')

mysqlCursor = mysql.cursor()

with open('data/mongo-iris.csv', newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)

    for doc in reader:
        sepal_length = int(doc['sepal_length'])
        sepal_width = int(doc['sepal_width'])
        petal_length = int(doc['petal_length'])
        petal_witdh = int(doc['petal_width'])
        varieties = doc['variety']

    query = "INSERT INTO from_csv(sepal_length, sepal_width, petal_length, petal_width, variety) VALUES (" + \
        sepal_length+", "+sepal_width+", "+petal_length + \
            ", "+petal_witdh+", '"+varieties+"')"

    print(query)

    mysqlCursor.execute(query)
    mysql.commit()
