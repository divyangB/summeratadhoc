#! /usr/lib/python3

import requests
from bs4 import BeautifulSoup

inn = input("Enter the text you want to search on wiki: ")   #ask query from user
search = "https://en.wikipedia.org/wiki/" + inn    #make a search for the query

page = requests.get(search)        #for making requests to the web page
soup = BeautifulSoup(page.text,'html.parser')

res = soup.select('.toc')           #selecting class for scrapping

for i in res:
	print (i.text)
