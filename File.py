#!/bin/bash/env python3
from bs4 import BeautifulSoup
import requests
import re
path = ''
linkList = []


class SearchItems:
    def __init__(self):
        term = input('Enter your searchterm: ')
        page = requests.get("http://www.google.de/search?q="+term)
        soup = BeautifulSoup(page.content, "lxml")
        links = soup.findAll("a")
        for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
            linkList.append(re.split(":(?=http)", link["href"].replace("/url?q=","")))
            with open(path, mode='wt', encoding='utf-8') as myfile:
                for lines in linkList:
                    myfile.write('\n'.join(str(line) for line in lines))
                    myfile.write('\n')
        print('File was written successfully')


SearchItems()
