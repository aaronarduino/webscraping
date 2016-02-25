from lxml import html
from bs4 import BeautifulSoup
import requests
import sys
import textwrap
from flask import Flask, json

app = Flask(__name__)

page = requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?product=Coffee&cart_id=1456352770.17889')
soup = BeautifulSoup(page.content, 'lxml')
tree = html.fromstring(page.content)

#This will create a list of buyers:
coffee_names = tree.xpath('//td[@bgcolor="#774B2E"]/b/font[@color="#FFFFFF"]/text()')

descriptions = soup('form')

coffees = []

for i in range(0, coffee_names.__len__()):
	coffees.append([coffee_names[i], descriptions[i+1].div.center.table('tr')[1].td.div.p.font.text.replace('\n', '').replace('\r', '')])

# print '\n\n'
# print 'Coffee: ' + coffees[int(sys.argv[1])][0] + '\n'
# print 'Description: ' 
# decwrap = textwrap.wrap(coffees[int(sys.argv[1])][1])
# for line in decwrap:
# 	print line
# print '\n\n'





@app.route("/coffee/<index>")
def hello(index):
    return 'Coffee: ' + coffees[int(index)][0] + '\n\nDescription: ' + coffees[int(index)][1]

if __name__ == "__main__":
    app.run()