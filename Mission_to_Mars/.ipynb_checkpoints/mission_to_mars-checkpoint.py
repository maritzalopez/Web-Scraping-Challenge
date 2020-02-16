#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd
import requests


# ### NASA Mars News

# In[ ]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)



# In[28]:


news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)


# In[29]:


html = browser.html
soup = BeautifulSoup(html,'html.parser')


# In[30]:


news_title = soup.find('div', class_= 'content_title').get_text()
news_title


# In[31]:


news_p = soup.find('div', class_ = 'article_teaser_body').get_text()
news_p


# ### JPL Mars Space Images - Featured Image

# In[68]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
basic_url = 'http://www.jpl.nasa.gov'
browser.visit(img_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[69]:


find_img = soup.find('img', class_='thumb').attrs['src']
find_img


# In[70]:


featured_img = basic_url + find_img
featured_img


# ### Mars Weather

# In[11]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

twitter_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(twitter_url)


# In[12]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[13]:


mars_weather = soup.find('p', class_='TweetTextSize').get_text()
mars_weather


# ### Mars Facts

# In[14]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

facts_url = 'https://space-facts.com/mars/'
browser.visit(facts_url)


# In[15]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[16]:


factstable = pd.read_html(facts_url)
factstable


# In[19]:


df = factstable[0]
df.columns = ['Mars Planet Profile', 'Details']
df


# In[20]:


df.set_index('Mars Planet Profile', inplace = True)
df


# In[21]:


html_table = df.to_html()
html_table


# In[22]:


html_table.replace('\n', '')


# In[23]:


df.to_html('table.html')


# ### Mars Hemispheres

# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemisphere_url)


# In[3]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[4]:


sidebar = soup.find_all('div', class_='item')
sidebar


# In[20]:


hemisphere_image_urls = []

for s in sidebar:
    title = (s.find('h3').text)
    browser.find_by_tag('h3').click()
    img_url = s.find('a')['href']
    hemisphere_image_urls.append({'title': title, 'img_url': 'https://astrogeology.usgs.gov' + img_url +'.tif/full.jpg'})
    
hemisphere_image_urls


# In[ ]:




