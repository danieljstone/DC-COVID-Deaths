#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:06:43 2021

@author: danielstone
"""


import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup
import re
import requests
import time

deaths=pd.read_csv("output.csv",index_col=0)

def deathupdate():
    global deaths
    daterange=pd.date_range(deaths["date"].iloc[-1],dt.date.today())
    def deathurl(date):
        if date >= dt.date.today():
            return None
        else:
            url="https://coronavirus.dc.gov/release/coronavirus-data-"+date.strftime("%B-%-d-%Y")
            return url
    for date in daterange[1:]:
        url=deathurl(date)
        if url == None:
            pass
        else:
            print(url)
            req = requests.get(url)
                # this fixes an annoying problem where some dates without reports redirect to pages for other dates
            if req.url == url:
                soup=BeautifulSoup(req.text, "lxml")    
                date=soup.select("div.content.clearfix > div.field.field-name-field-date.field-type-date.field-label-hidden > div > div > span").__str__().split('\"')[3][:10]
                b=soup.find_all(string=re.compile("year-old"))
                for x in b:
                    newline={}
                    newline["date"]=date
                    y=x.__str__().split()
                    newline["age"]=y[0].split("-")[0]
                    newline["gender"]=y[1]
                    newline["url"]=url
                    deaths=deaths.append(newline, ignore_index=True)
            else:
                pass
            time.sleep(3)
            
deathupdate()

deaths["date"]=pd.to_datetime(deaths.date)
deaths["age"]=deaths.age.astype(int)

deaths.to_csv("output.csv")