#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import urllib.request


# In[3]:


url = input("please input the address：");
with urllib.request.urlopen(url) as response:
    html = response.read()
soup = BeautifulSoup(html, 'html.parser')


# In[4]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[ ]:




