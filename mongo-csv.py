import csv

from pymongo import MongoClient

# MongoDB Connection
mongo = MongoClient('mongodb://localhost')
mongoCursor = mongo.dicoding_scrape

with open('data/dicoding_scrape.csv', 'w', newline='') as csvfile:

    # csv setting
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    result = mongoCursor.id.find()

    writer.writerow(['name', 'job', 'quotes'])

    # print result
    for data in result:

        name = data['name']
        job = data['job']
        quotes = data['quotes']

        writer.writerow([name, job, quotes])
