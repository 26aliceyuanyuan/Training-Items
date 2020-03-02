#!/usr/bin/env python
# coding: utf-8

# In[48]:


import requests 
from requests import request
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen


# In[49]:


def get_random_url():
    page = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    return page.url


# In[50]:


def get_page_hyperlinks(url):
    content=urlopen(url).read()
    BeautS=BeautifulSoup(content,'html.parser')
    return (BeautS.find(id='mw-content-text')).find_all('a',attrs={'href':re.compile('/wiki/')})


# In[56]:


def get_recursive_links(beginurl,targeturl,depth):
    content=get_page_hyperlinks(beginurl)
    if content==None:
        print('The page ( ',biginurl,' ) has no hyperlinks.')
        return True
    if recursive_path.get(beginurl)==None:
        links_in_page = set()#集合
        for hyl in content:
            link=hyl['href']
            if not (':' in link):
                if link.startswith('/') and not link.startswith('//'):
                    link=HOST+hyl['href']
                if urlparse(link).netloc==DOMAIN:#network location part is right
                    links_in_page.add(link)
            if str(link)==targeturl:
                recursive_path[beginurl]=links_in_page
                return True
        recursive_path[beginurl]=links_in_page
        print(recursive_path)
        if not (depth<=0):
            for each in links_in_page:
                stop=get_recursive_links(each,targeturl,depth=depth-1)
                if stop:
                    break


# In[52]:


def way_to_target(recursive_path,beginurl,targeturl,path=[]):
    path=path+[beginurl]
    if beginurl==targeturl:
        return path
    if recursive_path.get(beginurl)==None:
        return None
    for each in recursive_path[beginurl]:
        if each not in path:
            Npath=way_to_target(recursive_path,each,targeturl,path)
            if Npath:
                return Npath
    return None


# In[66]:


beginurl = 'https://en.wikipedia.org/wiki/Henan_(disambiguation)'
targeturl = 'https://en.wikipedia.org/wiki/Tibetan_people'
DOMAIN='en.wikipedia.org'
HOST='https://'+DOMAIN
recursive_path={}


# In[67]:


stop=False
#urllinks=get_recursive_links(url_1,url_2,4,list(recursive_path.keys()))
#print(urllinks)
get_recursive_links(beginurl,targeturl,10)


# In[68]:


result=way_to_target(recursive_path,beginurl,targeturl)


# In[69]:


if result==None:
    print('No result!')
else:
    print('The links between ',beginurl,' and ',targeturl)
    print(result)


# In[ ]:




