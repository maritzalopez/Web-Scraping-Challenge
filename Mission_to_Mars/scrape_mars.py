#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests


# ### NASA Mars News

# In[ ]:
def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    time.sleep(10)


    html = browser.html
    soup = BeautifulSoup(html,'html.parser')


    news_title = soup.find('div', class_= 'content_title').get_text()

    news_p = soup.find('div', class_ = 'article_teaser_body').get_text()


    # ### JPL Mars Space Images - Featured Image

    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    basic_url = 'http://www.jpl.nasa.gov'
    browser.visit(img_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    find_img = soup.find('img', class_='thumb').attrs['src']
    find_img


    featured_img = basic_url + find_img
    featured_img


    # ### Mars Weather

    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)
   

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find('p', class_='TweetTextSize').get_text()
    mars_weather

    # ### Mars Facts

    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    factstable = pd.read_html(facts_url)
    factstable

    df = factstable[0]
    df.columns = ['Mars Planet Profile', 'Details']
    df

    df.set_index('Mars Planet Profile', inplace = True)
    df

    html_table = df.to_html()
    html_table

    html_table.replace('\n', '')

    df.to_html('table.html')


    # ### Mars Hemispheres


    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    sidebar = soup.find_all('div', class_='item')
    sidebar


    hemisphere_image_urls = []

    for s in sidebar:
        title = (s.find('h3').text)
        browser.find_by_tag('h3').click()
        img_url = s.find('a')['href']
        hemisphere_image_urls.append({'title': title, 'img_url': 'https://astrogeology.usgs.gov' + img_url +'.tif/full.jpg'})
        
    hemisphere_image_urls

    allmarsinfo = {}
    allmarsinfo['news_title'] = news_title
    allmarsinfo['news_p'] = news_p
    allmarsinfo['featured_img'] = featured_img
    allmarsinfo['mars_weather']= mars_weather
    allmarsinfo['html_table']=html_table
    allmarsinfo['hemisphere_image_url'] = hemisphere_image_urls

    return allmarsinfo

# In[ ]:




