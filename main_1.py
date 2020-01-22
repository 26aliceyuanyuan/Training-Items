from requests import request
from bs4 import BeautifulSoup

import time
import re

def clearResFile():
    f=open('./results.txt','w')
    f.write('')
    f.close()
    f=open('./hrefs.txt','w')
    f.write('')
    f.close()

def downloadHref(href):
    return request('GET', href).text

def cond(i,text):
    return True if re.search(i, text) else False

def condition(text):
    # strings = ['республик[^ ]+ парт[^ ]+ соед[^ ]+ штат[^ ]+','демократ[^ ]+ парт[^ ]+ соед[^ ]+ штат[^ ]+','демократ[^ ]+ парт[^ ]+ США','республик[^ ]+ парт[^ ]+ США'] 
    params = ['владимир[^ ]+ путин[^ ]+']
    return max([cond(i,text) for i in params])

def clearExtraWhitespace(text):
    while(text.find("  ")>=0):
        text=text.replace("  "," ")
    while(text.find("\n\n")>=0):
        text=text.replace("\n\n","\n")
    return text


clearResFile()

for j in range(0,360*24):
    f=open('./hrefs.txt','r')
    hrefs=f.read().split('\n')
    f.close()
    htmlTexts =downloadHref('https://lenta.ru/parts/news')
    BeautS = BeautifulSoup(htmlTexts, 'lxml')
    newsItems = BeautS.findAll("div", {"class" : "item news"})
    f=open('./hrefs.txt','a')
    res=open('./results.txt','a')
    index=len(hrefs)
    for newsItem in newsItems:
        href=BeautifulSoup(str(newsItem), 'lxml').findAll("a")[1]['href']
        if (href.find('http')==-1):
            href='https://lenta.ru'+href
        if not (href in hrefs):
            f.write(href+'\n')
            if (href.find('https://lenta.ru'))>=0:
                BeautS=BeautifulSoup(downloadHref(href),'lxml')                
                Headline=BeautS.find("h1", {"class" : "b-topic__title"}).text
                Сontent=BeautS.find("div", {"class" : "js-topic__text"}).text.split('\n')[0]
                Source=BeautS.find("div", {"class" : "b-label__credits"}).text if BeautS.find("div", {"class" : "b-label__credits"})!=None else ""
                Source=Source[Source.find(':')+1:len(Source)]
                Content=clearExtraWhitespace(Сontent)
                # print(Source)
                if(condition(Headline.lower()))or(condition(Сontent.lower())):
                    res.write("\n"+str(index)+"\nНазвание: "+Headline+"\nСодержание: "+Сontent+"\nИсточник: "+Source)
                    index+=1
    res.close()
    f.close()
    time.sleep(10)
