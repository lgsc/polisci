import urllib
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

def get_souptable(url):
    soup = make_soup(url)
    data_dict = dict()
    for row in soup.findAll('tr'):
        i = -1
        for column in soup.findAll('td'):
            i = i + 1
            b = str(i)
            data_dict[b] = column.text
    return data_dict
