import urllib.request
from bs4 import BeautifulSoup
import re

import csv

with open('data/scrape_csv.csv', 'w', newline='') as csvfile:

    # csv setting
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    writer.writerow(['title', 'link'])

    # url = 'https://news.detik.com/berita/d-6026440/demo-bem-si-11-april-begini-rekayasa-lalu-lintas-di-sekitar-gedung-dpr'
    url = 'https://news.detik.com/'

    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    responData = res.read()

    # print(responData)

    title = re.findall(r'<title>(.*?)</title>', str(responData))
    date = re.findall(
        r'<div class="detail__date">(.*?)</div>', str(responData))
    author = re.findall(
        r'<div class="detail__author">(.*?)<span class="detail__label">', str(responData))

    title2 = re.findall(
        r'<div class="ai_replace_title" style="display:none">(.*?)</div>', str(responData))
    link = re.findall(r'i-link=(.*?)i-img-qs=', str(responData))

    # custom resource

    def normalization(text):
        text = text.replace("\\n", "")
        text = text.replace("\\'", "")
        text = text.strip()

        return text

    for i in range(len(title2)):

        getTitle = normalization(title2[i])
        getLink = normalization(link[i])

        writer.writerow([getTitle, getLink])
