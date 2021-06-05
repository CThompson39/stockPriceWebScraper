import requests
from requests import get
from bs4 import BeautifulSoup

def priceTracker():
	url = "https://finance.yahoo.com/quote/INTC?p=INTC&.tsrc=fin-srch"
	results = requests.get(url)
	soup = BeautifulSoup(results.text, "html.parser")
	price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
	
	return(price)

print("Intel's current price is " +priceTracker())
