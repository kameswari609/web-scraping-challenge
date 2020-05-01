#import dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
import os
import pandas as pd
import time
import re
from selenium import webdriver

def init_browser():
     
    executable_path = {"executable_path":"C:\webdrivers\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()
    mars_data = {}

    url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

    #scrapping latest news about mars from nasa
    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    mars_data['news_title'] = news_title
    mars_data['news_paragraph'] = news_paragraph 
    
    #Mars Featured Image
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    time.sleep(2)

    from urllib.parse import urlsplit
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
    
    

    #bring the full resolution image
    full_image = browser.find_by_id('full_image')
    full_image.click()
    
                       
    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()                   
    
    #get image url using BeautifulSoup
    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")
    # find the relative image url
    img_url_rel = soup.select_one('figure.lede a img').get("src")
    full_img_url = base_url + img_url_rel
    mars_data["featured_image"] = full_img_url
    
                   
                       
                       
                       

    #get mars weather's latest tweet from the website
    #url_weather = "https://twitter.com/marswxreport?lang=en"
    #browser.visit(url_weather)
    #html = browser.html
    #weather_soup = BeautifulSoup(html, 'html.parser')
    #mars_weather_tweet = weather_soup.find('span', text = re.compile('2020-04-27')).text
    #mars_data["mars_weather"] = mars_weather_tweet

    #Mars Facts

    fact_url = "https://space-facts.com/mars/"
    browser.visit(fact_url)
    time.sleep(2)
    table = pd.read_html(fact_url)
    

    df_mars_facts = table[0]
    df_mars_facts.columns = ["attribute", "Values"]
    mars_table = df_mars_facts.set_index(["attribute"])
    mars_html_table = mars_table.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    mars_data["mars_facts_table"] = mars_html_table

    #Mars Hemisperes

    url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemisphere)

    #Getting the base url
    hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_hemisphere))
    hemisphere_img_urls = []
    hemisphere_img_urls

    #Cerberus-Hemisphere-image-url

    
    results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(2)

    cer_img = browser.find_by_id('wide-image-toggle')
    cer_img.click()


    cerberus_image = browser.html
    soup = BeautifulSoup(cerberus_image, "html.parser")
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = hemisphere_base_url + cerberus_url
    cerberus_title = soup.find("h2",class_="title").text
    back_button = browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    hemisphere_img_urls.append(cerberus)


    #Schiaparelli-Hemisphere-image-url

    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)

    sch_img = browser.find_by_id('wide-image-toggle')
    sch_img.click()


    sch_image = browser.html
    soup = BeautifulSoup(sch_image, "html.parser")
    sch_url = soup.find("img", class_="wide-image")["src"]
    sch_img_url = hemisphere_base_url + sch_url
    sch_title = soup.find("h2",class_="title").text
    back_button = browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    Schiaparelli  = {"image title":sch_title, "image url": sch_img_url}
    hemisphere_img_urls.append(Schiaparelli)


    #Syrtis Major Hemisphere

    results2 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(2)

    syr_img = browser.find_by_id('wide-image-toggle')
    syr_img.click()


    syr_image = browser.html
    soup = BeautifulSoup(syr_image, "html.parser")
    syr_url = soup.find("img", class_="wide-image")["src"]
    syr_img_url = hemisphere_base_url + syr_url
    syr_title = soup.find("h2",class_="title").text
    back_button = browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    Syrtis   = {"image title":syr_title, "image url": syr_img_url}
    hemisphere_img_urls.append(Syrtis)


    #Valles Marineris Hemisphere

    results3 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)

    valles_img = browser.find_by_id('wide-image-toggle')
    valles_img.click()
    valles_image = browser.html
    soup = BeautifulSoup(valles_image, "html.parser")
    valles_url = soup.find("img", class_="wide-image")["src"]
    valles_img_url = hemisphere_base_url + valles_url
    valles_title = soup.find("h2",class_="title").text
    back_button = browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    Valles  = {"image title": valles_title, "image url": valles_img_url}
    hemisphere_img_urls.append(Valles)


    mars_data["hemisphere_img_url"] = hemisphere_img_urls

    

    return mars_data