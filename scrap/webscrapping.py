#!/usr/bin/python3

import requests
import bs4

#we have to make a request for the data

res= requests.get('http://www.bcci.tv/')

soup= bs4.BeautifulSoup(res.text,'lxml')
print(type(soup))


