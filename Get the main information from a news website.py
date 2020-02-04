#!/usr/bin/env python
# coding: utf-8

# In[78]:


from requests import request
from bs4 import BeautifulSoup
import time
import re


# In[79]:


#get Href from web
def acquirehref(href):
    return request('GET', href).text


# In[80]:


def format(text):
    while(text.find("  ")>=0):
        text=text.replace("  "," ")
    while(text.find("\n\n")>=0):
        text=text.replace("\n\n","\n")
    return text


# In[81]:


h=open('./hrefs.txt','w')
h.write('')
h.close()
res=open('./newsinfo.txt','w')
res.write('')
res.close()


# In[82]:


for j in range(0,1*2):
    h=open('./hrefs.txt','r')
    h.close()
    htmltext=acquirehref('https://russian.rt.com/trend/335110-ssha')
    BeautS=BeautifulSoup(htmltext,'lxml')
    BeautS.encoding = 'utf-8' 
    itemsnews=BeautS.findAll('div',{'class':'card__heading card__heading_all-new'})
    #print(itemsnews)
    h=open('./hrefs.txt','a+')
    res=open('./newsinfo.txt','a+')
    total=len(hrefs)
    #print(itemsnews)
    for itemnews in itemsnews:
        href=BeautifulSoup(str(itemnews),'lxml')
        href=href.find('a') 
        link=href.get('href')
        if(link.find('https')==-1):
            link='https://russian.rt.com/'+link
        if not (link in itemnews):
            h.write(link+'\n')
            if (link.find('https://russian.rt.com/'))>=0:
                BeautS=BeautifulSoup(acquirehref(link),'lxml')
                BeautS.encoding = 'utf-8' 
                for tag in BeautS.find_all('div', class_='article article_article-page'):  
                    title = tag.find('h1',class_="article__heading article__heading_article-page").get_text()
                    title=format(title.lower())
                #contents=BeautS.find('div',{'class':'caas-body'}).text
                #contents=format(contents)
                #author=BeautS.find('div', {'class':'author-name'}).text if BeautS.find('div', {'class':'author-name'})!=None else""
                for tag in BeautS.find_all('div', class_='article article_article-page'):  
                    abstract = tag.find('div',class_="article__summary article__summary_article-page js-mediator-article").get_text()
                    abstract=format(abstract.lower())
                for tag in BeautS.find_all('div', class_='article__date-autor-shortcode article__date-author-shortcode_article-page'):  
                    author = tag.find('div',class_="article__author article__author_article-page article__author_with-label").get_text()
                    author=format(author.lower())
                total+=1
                res=open('./newsinfo.txt','a+', encoding='utf-8')
                print('\n'+'This is '+str(total)+' news.The title is: '+title+'. The author is:'+author+'. The abastract is: '+abstract)
                res.write('\n'+'This is '+str(total)+' news.The title is: '+title+'. The author is:'+author+'. The abastract is: '+abstract)
                #


# In[83]:


res.close()
h.close()
time.sleep(10)


# In[ ]:




