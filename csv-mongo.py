import csv

from pymongo import MongoClient

# MongoDB Connection
mongo = MongoClient('mongodb://localhost')
mongoCursor = mongo.csvmongo

with open('data/iris.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)

    for row in reader:
        print(row)

        sepal_length = row[0]
        sepal_width = row[1]
        petal_length = row[2]
        petal_witdh = row[3]
        varieties = row[4]

        mongoFormat = {"sepal_length": sepal_length, "sepal_width": sepal_width,
                       "petal_length": petal_length, "petal_width": petal_witdh, "variety": varieties}
        print(mongoFormat)

        # insert into mongo
        mongoCursor.irisdata.insert_one(mongoFormat)
