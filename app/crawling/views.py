import urllib.request

from bs4 import BeautifulSoup
from django.shortcuts import render


def get_soup(target_url):
    html = urllib.request.urlopen(target_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def extract_data(soup):
    table = soup.find('table', {'class': 'grid'})
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx > 0:
            tds = tr.find_all('td')
            sequence = tds[0].text.strip()
            description = tds[1].text.strip()
            solved_num = tds[2].text.strip()
            print(sequence, description, solved_num)


for i in range(1, 7):
    target_url = 'http://euler.synap.co.kr/prob_list.php?pg={}'.format(i)
    soup = get_soup(target_url)
    extract_data(soup)


def detail(request):
    return render(request, 'crawling/crawling.html')