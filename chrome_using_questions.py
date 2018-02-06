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



browser = Browser('chrome', executable_path='chromedriver', headless=False)

urls = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced', 
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']

#define empty lists
titles_list = []
image_urls_list= []

for url in urls:
    browser.visit(url)
    soup = BeautifulSoup(browser.html, 'html.parser')
    soup_1 = soup.find('section', class_="block metadata")
    headers = soup_1.find('h2', class_='title')
    cleaned_title = headers.get_text().strip("Enhanced")
    titles_list.append(cleaned_title)

    soup_links = soup.find('div', class_="downloads")
    possible_links = soup_links.find_all('a')
    for link in possible_links:
        links_0 = link.attrs['href']
        image_urls_list.append(links_0)

 
print(titles_list)
print(image_urls_list)