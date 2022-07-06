import urllib.request
from bs4 import BeautifulSoup
import re

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


# cleaning text
def normalization(text):
    text = text.replace("\\n", "")
    text = text.replace("\\'", "")
    text = text.strip()

    return text


# loop for all getted data
for i in range(len(name)):

    getName = normalization(name[i])
    getJob = normalization(job[i])
    getQuotes = normalization(quotes[i])

    # print all getted item
    print(i)
    print(normalization(getName))
    print(normalization(getJob))
    print(normalization(getQuotes))
