def main():
    # coding: utf-8

    import re
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd



    # 1. Scrape Mars News Website

    url_1 = "https://mars.nasa.gov/news/"
    html_1 = requests.get(url_1)
    soup_1 = BeautifulSoup(html_1.text, 'html.parser')

    results1 = soup_1.find('div', class_='content_title')
    news_title = results1.text.strip()
    print(news_title)

    results2 = soup_1.find('div', class_='image_and_description_container')

    news_body = results2.text.strip()
    print(news_body)



    # .2 - Scrape Mars Featured Image (not working in Jupyter Notebook - working in Python)

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



    # 3. Scrape Twitter

    url_2 = "https://twitter.com/marswxreport?lang=en"
    html_2 = requests.get(url_2)
    soup_2 = BeautifulSoup(html_2.text, 'html.parser')

    tweet_1 = soup_2.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    #print(tweet_1.prettify())

    weather_tweet = tweet_1.text
    print(weather_tweet)



    # .4. Scrape Mars Facts

    url = 'https://space-facts.com/mars/'

    table_data = pd.read_html(url)
    table_data

    mars_df = table_data[0]
    mars_df.columns = ['description','value']
    mars_df.to_html('mars_table.html', index=False)
    #get_ipython().system('open mars_table.html')



    # .5. Scrape Hemisphere links ((not working in Jupyter Notebook - working in Python)

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


main()


# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders hello_world.html template
@app.route("/")
def echo():
    return render_template("index.html", image_urls_list=image_urls_list)


if __name__ == "__main__":
    app.run(debug=True)
