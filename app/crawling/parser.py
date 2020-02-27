import json
import os

import requests
from bs4 import BeautifulSoup

# python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# HTTP GET Request
req = requests.get('https://bomi.github.io/beomi.github.io_old/')

# HTML 소스 가져오기
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# CSS Selector를 통해 html요소들을 찾아낸다.
my_titles = soup.select(
    'h3 > a'
)

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)
