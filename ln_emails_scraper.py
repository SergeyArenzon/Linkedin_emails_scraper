#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests,os,random,sys,time,urllib.request,re
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup


# In[30]:


#loc = "/home/sergey/jupyter_projects/chromedriver"
class LNScraper:
    
    def __init__(self,myId,myPass,webDriverLoc):
        self.webDriverLoc = webDriverLoc
        self.myPass = myPass
        self.myId = myId
        

    def getEmailsFromUrl(self,url):
        
        browser = webdriver.Chrome(self.webDriverLoc)
        loginPage = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
        browser.get(loginPage)

        elementID = browser.find_element_by_id("username")
        elementPASS = browser.find_element_by_id("password")

        elementID.send_keys(self.myId)
        elementPASS.send_keys(self.myPass)
        elementPASS.submit()
        #url = "https://www.linkedin.com/posts/guy-zwerdling_javascript-php-jquery-activity-6601806961535254528-yU-E"

        browser.get(url)

        src = browser.page_source

        soup = BeautifulSoup(src,'html.parser')

        email = []
        emails = soup.find_all("a", href=re.compile("mailto:"))

        for i in emails:
            email.append(i["href"].split(":")[1])

        

