import os

import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

from crawling.models import CrawlingData


def parse_blog():
    req = requests.get('https://bomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
    )
    data = {}

    for title in my_titles:
        data[title.text] = title.get('href')
    return data


if __name__ == '__main__':
    crawling_data_dict = parse_blog()
    for t, l in crawling_data_dict.items():
        CrawlingData(title=t, link=l).save()
