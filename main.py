from lxml import html
import requests
import sys

page = requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?product=Coffee&cart_id=1456352770.17889')
tree = html.fromstring(page.content)

#This will create a list of buyers:
coffee_names = tree.xpath('//td[@bgcolor="#774B2E"]/b/font[@color="#FFFFFF"]/text()')

descriptions = tree.xpath('//tr/td[@valign="top"]/div[@align="left"]/p/font[@size="2"]/text()')

coffees = []

for i in range(0, coffee_names.__len__()):
	coffees.append([coffee_names[i], descriptions[i]])

print coffees[int(sys.argv[1])]