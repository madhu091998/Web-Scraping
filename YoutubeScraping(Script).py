#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing necessary packages

from selenium import webdriver
import csv
import pandas as pd
import time


# In[6]:


#Reading the csv file containing youtube video links
links = pd.read_csv("youtube_scraping.csv",header=None)

#DRIVER_PATH is the path in my computer where I have installed chromedriver
DRIVER_PATH = "D:\DataQuest\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


# In[7]:


#Creating a csv file to store the data
csv_file = open("data_youtube.csv",'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["video_link","video_views","uploaded_date","comments","likes","dislikes"])


# In[8]:


#Scraping

#Looping through the links
for n in range(500):
    link = links[0][n]
    driver.get(link)

    #Suspending the execution for 3 seconds until the page loads in chromedriver
    time.sleep(3)
   

    #url
    url = driver.current_url

    #views
    views = driver.find_element_by_xpath("//span[@class='view-count style-scope yt-view-count-renderer']").text.split(" ")[0]
    
    #uploaded_date
    uploaded_date = driver.find_elements_by_xpath("//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']")[1].text

    #likes and dislikes
    content = driver.find_elements_by_xpath("//yt-formatted-string[@class='style-scope ytd-toggle-button-renderer style-text']")
    likes = content[0].text
    dislikes = content[1].text

    #number_of_comments
    #This code is used to scroll the webpage so that the comments sections become visible
    driver.execute_script("window.scrollTo(0, 500)") 

    #Suspending the execution for 3 seconds until the page loads in chromedriver
    time.sleep(3)
    num_comments = driver.find_element_by_xpath("//yt-formatted-string[@class='count-text style-scope ytd-comments-header-renderer']").text.split(" ")[0]
    #Writing data into the file      
    csv_writer.writerow([url,views,uploaded_date,num_comments,likes,dislikes])

#Closing the file
csv_file.close()


# In[9]:


#Exiting chromedriver
driver.quit()


# In[ ]:




