import urllib.request
from bs4 import BeautifulSoup
import re

# upload to mysql
import mysql.connector

# Mysql Connection
mysql = mysql.connector.connect(
    host='localhost', password='', user='root', database='dicoding_scrape')
mysqlCursor = mysql.cursor()

url = 'https://www.dicoding.com/about'

req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
responData = res.read()


# print(responData)
name = re.findall(
    r'<h5><b>(.*?)</b></h5>', str(responData))
job = re.findall(
    r'<p class="text-muted mb-4"><b>(.*?)</b></p>', str(responData))
quotes = re.findall(
    r'<p data-equal-height="content">(.*?)</p>', str(responData))


# custom resource
def normalization(text):
    text = text.replace("\\n", "")
    text = text.replace("\\'", "")
    text = text.strip()

    return text


#  Loop for all getted data
for i in range(len(name)):

    getName = normalization(job[i])
    getJob = normalization(job[i])
    getQuotes = normalization(quotes[i])

    query = "INSERT INTO scrape(name, job, quotes) VALUES('" + \
        getName+"', '"+getJob+"', '"+getQuotes+"')"

    print(query)

    mysqlCursor.execute(query)
    mysql.commit()
