from flask import render_template, request, flash, redirect, abort, jsonify, json, url_for, Response
from jinja2 import TemplateNotFound
from lxml import html
from bs4 import BeautifulSoup
import requests
import sys
import textwrap

from . import app
from . import socketio
coffees = []


pages = [requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?product=Coffee&cart_id=1456352770.17889'),
  requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?next=12&cart_id=1456352770.17889&product=Coffee'),
  requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?next=24&cart_id=1456352770.17889&product=Coffee'),
  requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?next=36&cart_id=1456352770.17889&product=Coffee'),
  requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?next=48&cart_id=1456352770.17889&product=Coffee'),
  requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?next=60&cart_id=1456352770.17889&product=Coffee'),
  requests.get('http://www.spicemerchant.com/cgi-bin/store/commerce.cgi?next=72&cart_id=1456352770.17889&product=Coffee')]

for page in pages:
  soup = BeautifulSoup(page.content, 'lxml')
  tree = html.fromstring(page.content)

  #This will create a list of buyers:
  coffee_names = tree.xpath('//td[@bgcolor="#774B2E"]/b/font[@color="#FFFFFF"]/text()')

  descriptions = soup('form')

  for i in range(0, coffee_names.__len__()):
    coffees.append([coffee_names[i], descriptions[i+1].div.center.table('tr')[1].td.div.p.font.text.replace('\n', '').replace('\r', '')])

@app.route("/", methods=['GET'])
def root():
    try:
      return render_template('index' + '.html',
          title="Home", coffees=enumerate(coffees))
    except TemplateNotFound:
      abort(404)

@app.route("/coffee/<index>", methods=['GET'])
def details(index):
    try:
      return render_template('details' + '.html',
          title="Home", coffee=coffees[int(index)])
    except TemplateNotFound:
      abort(404)