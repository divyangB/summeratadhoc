#!/usr/bin/python3

import requests
import bs4
#asking for user query
inn=input("Ask your query... ")
#storing the query in a variable
search = "https://www.google.co.uk/search?q=" + inn
res = requests.get(search)
soup = bs4.BeautifulSoup(res.text,"html.parser")
anch= soup.findAll('a')
for i in anch:
	url=i.get('href')
	index=url.find('?q=')
	url=url[index+3::]
	if url.find('https://')==0:
		index=url.find('&')
		print(url[:index]+"\n")






