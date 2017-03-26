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

def get_orderedkeys(url):
    soup = make_soup(url)
    key_list = []
    for row in soup.findAll('tr'):
        i = -1
        for column in soup.findAll('td'):
            i = i + 1
            b = str(i)
            key_list.append(b)
    return key_list

def find_soupid(dictionary, substring):
    for key in dictionary:
        value = dictionary.get(key)
        if substring in value:
            return int(key)

def column_keys(first_num):
    x = 0
    num = first_num
    col_ids = []

    while x != 12:
        col_ids.append(str(num))
        num = num + 6
        x = x + 1
    return col_ids


# https://en.wikipedia.org/wiki/Puerto_Rico%27s_at-large_congressional_district#List_of_Resident_Commissioners
# https://en.wikipedia.org/wiki/List_of_Secretaries_of_State_of_Puerto_Rico
# https://en.wikipedia.org/wiki/List_of_mayors_of_San_Juan,_Puerto_Rico

key_list = get_orderedkeys("https://en.wikipedia.org/wiki/List_of_governors_of_Puerto_Rico")
data = get_souptable("https://en.wikipedia.org/wiki/List_of_governors_of_Puerto_Rico")

first_row_gov = "Luis Muñoz Marín"
last_row_gov = "Ricky Rosselló"

start_key = find_soupid(data, first_row_gov) - 1
stop_key = find_soupid(data, last_row_gov) + 4


subset_keys = key_list[start_key:stop_key+1]
subset_dict = {key: data[key] for key in subset_keys}

name_col_ids = column_keys(895)
office_in_ids = column_keys(896)
office_out_ids = column_keys(897)
island_party = column_keys(898)
us_party = column_keys(899)

col2_data = {key: data[key] for key in name_col_ids}
col2_data = list(col2_data.values())

col3_data = {key: data[key] for key in office_in_ids}
col3_data = list(col3_data.values())

col4_data = {key: data[key] for key in office_out_ids}
col4_data = list(col4_data.values())

col5_data = {key: data[key] for key in island_party}
col5_data = list(col5_data.values())

col6_data = {key: data[key] for key in us_party}
col6_data = list(col6_data.values())

print(col6_data)

#print(data.get(str(895)))
#print(data.get(str(901)))
