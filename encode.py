import requests
from bs4 import BeautifulSoup
import urllib
import sys

soup = BeautifulSoup(requests.get(str(sys.argv[1])).text)
for tag in soup.find_all("img"):
	tag["href"]=urllib.quote(requests.get(str(sys.argv[1])+tag["src"]).read().encode("base64"))

print soup.prettify()