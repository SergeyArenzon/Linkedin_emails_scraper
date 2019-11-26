#!/usr/bin/env python
# coding: utf-8

# In[142]:


import requests,os,random,sys,time,urllib.request,re
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup


# In[122]:


browser = webdriver.Chrome("/home/sergey/jupyter_projects/chromedriver")


# In[154]:


browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


# In[155]:


elementID = browser.find_element_by_id("username")
elementPASS = browser.find_element_by_id("password")

elementID.send_keys("sergeyr1991@gmail.com")
elementPASS.send_keys("typhoonn91")
elementPASS.submit()

html = "https://www.linkedin.com/posts/guy-zwerdling_javascript-php-jquery-activity-6601806961535254528-yU-E"
browser.get(html)

src = browser.page_source

soup = BeautifulSoup(src,'html.parser')

email = []
emails = soup.find_all("a", href=re.compile("mailto:"))

for i in emails:
    email.append(i["href"].split(":")[1])



