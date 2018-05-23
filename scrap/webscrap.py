#!/usr/bin/python3

import bs4
import requests

inn = input("Enter your query: \n")
search = "https://www.google.com/?q=" + inn
page = requests.get(search)
soup = bs4.BeautifulSearch(page.text,"html.parser")
anch= soup.findAll('a')
for i in anch:
	url = i.get('href')
	index = url.find("?q=")
	url = url[index+3::]
	if url.find('https://')==0:
		index = url.find('&')
		print(url[:index]+"\n") 


