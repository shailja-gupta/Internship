#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[ ]:


from bs4 import BeautifulSoup
import requests


# # 1) Write a python program to display all the header tags from wikipedia.org and make data frame

# In[120]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[121]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:


import pandas as pd


# In[122]:


header_tags = []

for i in soup.find_all('span',class_="mw-headline"):
    header_tags.append(i.text)
header_tags
    

df = pd.DataFrame({'Header':header_tags})
print(df)


# # 2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
# from https://currentaffairs.adda247.com/list-of-presidents-of-india/ and make data frame.
# 
# 

# In[123]:


page = requests.get('https://currentaffairs.adda247.com/list-of-presidents-of-india/')
page


# In[124]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:


president_list = []

for president in soup.select("tbody tr"):
    name = president.select('td')[0].text
    term = president.select('td')[1].text
    president_list.append((name, term))
president_list

df = pd.DataFrame(president_list, columns= ["Name", "Term"])
print(df)


# # 3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data framea) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team andrating.
# c) Top 10 ODI bowlers along with the records of their team andrating

# In[ ]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[ ]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:


teams = []

for i in soup.find_all('span', class_="u-hide-phablet"):
    teams.append(i.text)
teams

matches = []

for i in soup.find_all('td', class_="rankings-block__banner--matches"):
    matches.append(i.text)
matches




  


# # 4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data framea) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[ ]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/overview')
page


# In[ ]:


teams = []

for i in soup.find_all('span', class_="u-hide-phablet"):
    teams.append(i.text)
teams

matches = []

for i in soup.find_all('td', class_="rankings-block__banner--matches"):
    matches.append(i.text)
matches


# # 5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
# make data framei) Headline
# ii) Time
# iii) News Link

# In[ ]:


page=requests.get('https://www.cnbc.com/world/?region=world')
page


# In[ ]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:


headline = []

for i in soup.find_all('div', class_="LatestNews-headlineWrapper"):
    news.append(i.text)
    
headline

times = []

for i in soup.find_all('time', class_="LatestNews-timestamp"):
    times.append(i.text)
    
times

news_link= []

for i in soup.find_all('a', href="https://www.cnbc.com/2023/09/16/stellantis-offers-raises-inflation-protection-to-uaw-as-strikes-continue.html"):
    news_link.append(i.text)
    
news_link

df = pd.DataFrame({'Headline':headline, 'Times':times, 'News':news_link})
df


# # 6)Write a python program to scrape the details of most downloaded articles from AI in last 90
# days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details and make data framei) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL
# 

# In[ ]:


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[ ]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:


paper_title = []

for i in soup.find_all('h2', class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)
    
paper_title

authors = []

for i in soup.find_all('span', class_="sc-1w3fpd7-0 dnCnAO"):
    authors.append(i.text)
authors

publish_date = []

for i in soup.find_all('span', class_="sc-1thf9ly-2 dvggWt"):
    publish_date.append(i.text)

publish_date

paper_url = []
for i in soup.find_all('span',class_="sc-5smygv-0 fIXTHm"):
    paper_url.append(i.text)
paper_url

df = pd.DataFrame({'Title':paper_title, 'Author':authors, 'Publish_date':publish_date, 'Paper_url':paper_url})


# # 7)Write a python program to scrape mentioned details from dineout.co.inand make data framei) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[ ]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[ ]:


soup = BeautifulSoup(page.content)
soup


# In[ ]:


#i) Restaurant name
#ii) Cuisine iii) Location iv) Ratings v) Image URL

name = []

for i in soup.find_all('div', class_="restnt-info cursor"):
    name.append(i.text) # add title in the empty list one by one
    
name



loc = []

for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    loc.append(i.text) # add title in the empty list one by one
    
loc

rating = []
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    rating.append(i.text)
rating

image = []
for i in soup.find_all('img', class_="no-img"):
    image.append(i["data-src"])
image

df = pd.DataFrame({'Name':name,'Location':loc,'Rating':rating, 'Image':image})
df


# In[ ]:





# In[ ]:




