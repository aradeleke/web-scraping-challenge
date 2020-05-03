
import pandas as pd
import numpy as np
import requests
import time

from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver


##import requests
##from urllib import request, response, error, parse
#from urllib.request import urlopen


# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text

# In[2]:


get_ipython().system('which chromedriver')


# In[3]:


def init_browser():
    executable_path = {'executable_path':'/c/Users/aadol/Documents/bin/chromedriver'}
    browser = Browser('chrome', headless=False)
    return browser

def title_and_para():

    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    


    soup.title.contents


    #collect the latest News Title and Paragraph Text
    latest_title = soup.find('div', class_='rollover_description').text
    print(latest_title)

    #Paragraph Text
    para_text = soup.find('div', class_ = 'article_teaser_body')
    browser.quit()
    print(para_text.text)


# ### JPL Mars Space Images - Featured Image
def featured_image():

    browser = init_browser()
    executable_path = {'executable_path':'/c/Users/aadol/Documents/bin/chromedriver'}
    browser = Browser('chrome', headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(1)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    space_list = []
    results = soup.find_all("div", class_ = "img")
    for image in results:
        space_list.append(image.img["src"])
    

    space_image = []
    jpl_image = soup.find_all("div", class_ = "img")
    for image in results:
        space_image.append(image.img["src"])
    

    mars_image = space_image[0]

    mars_image_url = "https://www.jpl.nasa.gov" + feature_image

    print("Feature Image URL:", mars_image_url)

    browser.quit()
    mars_image_url


def mars_weather()
    browser = init_browser()

    executable_path = {'executable_path':'/c/Users/aadol/Documents/bin/chromedriver'}
    browser = Browser('chrome', headless=False)


    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    xpath = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/article/div/div[3]/div[1]/div/span"

    if browser.is_element_present_by_xpath(xpath, wait_time = 5):
        news = browser.find_by_xpath(xpath).text

    browser.quit()
    print(news)




def mars_facts
    browser = init_browser()


    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    mars_df = tables[0]
    mars_df.columns = mars_df.columns.astype(str)
    mars_df = mars_df.rename(columns = {"0": "Parameters", "1": "Values"})
    mars_df


def mars Hemispheres
    browser = init_browser()

    html_mars = mars_df.to_html(header=False, index=False)

    print(html_mars)

    executable_path = {'executable_path':'/c/Users/aadol/Documents/bin/chromedriver'}
    browser = Browser('chrome', headless=False)

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    base_url = "https://astrogeology.usgs.gov"

    mars_hemis = []
    img_hrefs = []
    results_title = soup.find_all("div", class_ = "description")
    for result in results_title:
        mars_hemis.append(result.h3.text)
        full_href = base_url + result.a["href"]
        img_hrefs.append(full_href)
    
    mars_hemis


#Save image URL
full_resolution_img = []

for i in range(len(img_hrefs)):
    url = img_hrefs[i]
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find("img", class_ = "wide-image")["src"]
    full_resolution = base_url + result
    full_resolution_img.append(full_resolution)
    
    full_resolution_img
    

hemis_image_urls = []
hemis_image_urls_dict = {}

for i in range(4):
    hemis_image_urls_dict["title"] = titles[i]
    hemis_image_urls_dict["img_url"] = full_resolution_img[i]
    hemis_image_urls.append(hemis_image_urls_dict)
    hemis_image_urls_dict = {}

browser.quit()
return hemis_image_urls

if __name__ == "__main__":
    print("\nTesting Data Retrieval:....\n")
    print(title_and_para())
    print(featured_image())
    print(mars_weather())
    print(mars_hemispheres())
    print("\nProcess Complete!\n")


# In[ ]:




