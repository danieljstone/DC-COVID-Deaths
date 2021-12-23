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

deaths=pd.read_csv("dc_covid_deaths.csv",index_col=0)

def deathupdate():
    global deaths
    daterange=pd.date_range(deaths["date"].iloc[-1],dt.date.today()- dt.timedelta(days=1))
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
                try:
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
                except:
                    pass
            else:
                pass
            time.sleep(3)
            
    deaths["date"]=pd.to_datetime(deaths.date)
    deaths["age"]=deaths.age.astype(int)
    deaths["age group"]=pd.cut(deaths["age"],[16, 19, 44, 64,200], precision=0, labels=["16-19","20-44","45-64","65+"])
    deaths["agedecade"]=pd.cut(deaths["age"],[0, 9, 19, 29,39,49,59,69,79,200], precision=0, labels=["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80+"])
    deaths.to_csv("dc_covid_deaths.csv")

#summary tables

    pd.pivot_table(deaths,index="age",values="date", columns="gender",aggfunc="count").fillna(0).to_csv("total_by_age_gender.csv")
    pd.pivot_table(deaths,index="age group",values="date", columns="gender",aggfunc="count").fillna(0).to_csv("total_by_age_group_gender.csv")
       
            
deathupdate()


#for off instances where the url format is different


def urlupdate(url):
   global deaths
   req = requests.get(url)
   try:
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
   except:
        pass
   else:
       time.sleep(3)








