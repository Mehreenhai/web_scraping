import re
from splinter import Browser
from bs4 import BeautifulSoup

browser = Browser('chrome', headless=False)
url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)

browser.click_link_by_partial_text('FULL IMAGE')
html2 = browser.html
soup2 = BeautifulSoup(html2, 'html.parser')

links = soup2.find('div', class_="carousel_items")

tag = links.find('a', class_='button fancybox')
link = "https://www.jpl.nasa.gov" + tag.get('data-fancybox-href')
print(link)

