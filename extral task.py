#!/usr/bin/env python
# coding: utf-8

# In[96]:


import re
import sys


# In[97]:


log=sys.argv[1]
ip=r"?P<ip>[\d.]*"
date=r"?P<date>\d+"
month=r"?P<month>\w+"
year=r"?P<year>\d+"
log_time=r"?P<time>\S+"
timezone=r"""?P<timezone>
                 [^\"]*
         """
name=r"""?P<name>\"
            [^\"]*\"     
        """
method=r"?P<method>\S+"
request=r"?P<request>\S+"
protocol=r"?P<protocol>\S+"
status=r"?P<status>\d+"
bodyBytesSent=r"?P<bodyBytesSent>\d+"
refer=r"""?P<refer>\"
             [^\"]*\"
             """
userAgent=r"""?P<userAgent>
                .*
               """


# In[98]:


log_fmt=r"(%s)\ \[(%s)/(%s)/(%s)\:(%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)"
p = re.compile( log_fmt%(ip, date, month, year, log_time,timezone,name,method,request,protocol,status,bodyBytesSent,refer,userAgent), re.VERBOSE)


# In[99]:


def getcode():
    codedic={}
    f=open(log,'r')
    for logline in f.readlines():
        matchs=p.match(logline)
        if matchs!=None:
            allGroups=matchs.groups()
            status=allGroups[10]
            codedic[status]=codedic.get(status,0)+1
    return codedic
    f.close()


# In[100]:


def getIP():
    f=open(log,'r')
    IPdic={}
    for logline in f.readlines():
        matchs=p.match(logline)
        if matchs!=None:
            allGroups=matchs.groups()
            IP=allGroups[0]
            IPdic[IP]=IPdic.get(IP,0)+1
        IPdic=sorted(IPdic.iteritems(),key=lambda c:c[1],reverse=True)
        IPdic=IPdic[0:11:1]
    return IPdic
    f.close()


# In[101]:


def getURL():
    f = open(log,'r')
    URLdic={}
    for logline in f.readlines():
        matchs = p.match(logline)
        if matchs !=None:
            allGroups =matchs.groups()
            urlname = allGroups[6] 
            URLdic[urlname] = URLdic.get(urlname,0) +1
    URLdic=sorted(URLdic.iteritems(),key=lambda c:c[1],reverse=True)
    URLdic=URLdic[0:11:1]           
    return URLdic


# In[102]:


def getpv():
    f=open(log,'r')
    pvdic={}
    for logline in f.readlines():
        matchs=p.match(logline)
        if matchs !=None:
            allGroups=matchs.groups()
            timezone=allGroups[4]
            time=timezone.split(':')
            minute=time[0]+":"+time[1]
            pvdic[minute]=pvdic.get(minute,0)+1
            pvdic=sorted(pvdic.iteritems(),key=lambda c:c[1],reverse=True)
            pvdic=pvdic[0:11:1]
    return pvdic


# In[103]:


if __name__=='__main__':
    print ("Website monitoring status check status code")#网站监控状况检查状态码
    getcode() 
    print ("The 10 most visited IP addresses on the site") #网站访问量最高的20个IP地址
    getIP()
    print ("20 most visited site names")#网站访问最多的10个站点名
    getURL()
    getpv()

