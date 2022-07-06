import mysql.connector
from pymongo import MongoClient

# Mysql Connection
mysql = mysql.connector.connect(host='localhost', password='', user='root')

mysqlCursor = mysql.cursor()

# MongoDB Connection
mongo = MongoClient('mongodb://localhost')
mongoCursor = mongo.dicoding_scrape

# Migration Target
database = 'dicoding_scrape'
table = 'scrape'

# Taking Data from Mysql
mysqlCursor.execute('USE {};'.format(database))
mysqlCursor.execute('SELECT * FROM {};'.format(table))

# Menguraikan hasil select dalam bentuk array
result = mysqlCursor.fetchall()


# print(result)
for row in result:
    data = []
    # print(row)
    for data_column in row:
        # print(data_column)
        data.append(data_column)
    print(data)

    mongoFormat = {"id": data[0], "name": data[1],
                   "job": data[2], "quotes": data[3]}
    print(mongoFormat)
    print()

    mongoCursor.id.insert_one(mongoFormat)
