#! /usr/lib/python3

import requests
from bs4 import BeautifulSoup

inn = input("Enter the text you want to search on wiki: ")
search = "https://en.wikipedia.org/wiki/" + inn

page = requests.get(search)
soup = BeautifulSoup(page.text,'lxml')

res = soup.findAll('span')

for i in res:
	print(i.text)
