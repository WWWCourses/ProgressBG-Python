from urllib import request,parse,error
from bs4 import BeautifulSoup
from collections import OrderedDict
from operator import itemgetter    
import re


def get_html_content(url):
	if url.startswith("http"):
		# make the request
		req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

		respone = request.urlopen(req)
		return respone.read()
	else:
		with open(url,"r") as f:
		  return f.read()

def get_products(content):
	bs_parser = BeautifulSoup(content, 'html.parser')
	return bs_parser.find('ul', 'products')

def scrape_data(products_html):
	for product in products_html.find_all("article"):	
		try:
			name = product.select("div h2")[0].string
		except:
			name = "NoName"

		try:
			price = product.select("div tspan")[0].string
		except:
			price = None
			
		products.append((name,int(price)))

def print_scraped_data(products):
	sorted_by_price = sorted(products, key=lambda p: p[1])
	for i in sorted_by_price:
		# print(i)
		print("{} - {}".format(i[0],i[1]))


start_url = "https://laptop.bg/laptops-lenovo?page="
# start_url = "to_scrape.html"
products = []

for i in range(10,16):
	url = start_url+str(i)
	print("Scraping URL:", url)
	products_html = get_products( get_html_content(url) )
	scrape_data(products_html)
	
print_scraped_data(products)



