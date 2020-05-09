from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time


def init_browser():
    
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
    
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    article_heading_list = []

    for article_heading in soup.find_all('div',class_="content_title"):
    
        try:        
            article_heading_list.append(article_heading.find('a').text)
        except:
            pass
        
    news_title = article_heading_list[0]

    article_paragraph_list = []

    for article_para in soup.find_all('div',class_="article_teaser_body"):
        
        try:        
            article_paragraph_list.append(article_para.text)
        except:
            pass

    news_p = article_paragraph_list[0]

    title_paragraph_dict = {"news_title": news_title, "news_p": news_p}

    browser.quit()

    return title_paragraph_dict


# ### JPL Mars Space Images - Featured Image
def mars_image():

    browser = init_browser()
    
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
    mars_image = soup.find_all("div", class_ = "img")
    for image in results:
        space_image.append(image.img["src"])
    

    mars_image = space_image[0]

    mars_image_url = "https://www.jpl.nasa.gov" + mars_image

    mars_image_dict = {"image": mars_image_url}

    browser.quit()

    return mars_image_dict


""" def mars_weather():
    browser = init_browser()


    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    xpath = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/article/div/div[3]/div[1]/div/span"

    if browser.is_element_present_by_xpath(xpath, wait_time = 5):
        news = browser.find_by_xpath(xpath).text

    mars_weather_dict = {"mars_weather": news}

    browser.quit()
    return mars_weather_dict"""



def mars_facts():
    browser = init_browser()

    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    mars_df = tables[0]
    mars_df.columns = mars_df.columns.astype(str)
    mars_df = mars_df.rename(columns = {"0": "Parameters", "1": "Values"})
    mars_df
    mars_df_to_html = mars_df.to_html("mars_facts_table.html")

    mars_df_to_html_dict = {"mars_fact": mars_df_to_html}

    return mars_df_to_html_dict



def mars_hemis():
    browser = init_browser()

    
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
        # hemis_image_urls_dict["title"] = title[i]
        hemis_image_urls_dict["img_url"] = full_resolution_img[i]
        hemis_image_urls.append(hemis_image_urls_dict)
        hemis_image_urls_dict = {}

    browser.quit()
    return hemis_image_urls

if __name__ == "__main__":
    print("\nTesting Data Retrieval:....\n")
    print(title_and_para())
    print(mars_image())
    # print(mars_weather()) 
    print(mars_hemis()) 
    print("\nProcess Complete!\n")


# In[ ]:




