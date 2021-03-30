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


problem_page_data=pd.read_csv("problem_page_data.csv")
problem_page_data["date"]=pd.to_datetime(problem_page_data.date)

deaths=pd.DataFrame(columns=["date"])

def deathdata(start_date,end_date):
    global deaths
    daterange=pd.date_range(start_date,end_date)
    def deathurl(date):
        #will pull all previous dates
        if date >= dt.date.today():
            return None
        # will pull from the larger list
        elif date < dt.datetime (2020,4,13):
            return None
        #no report
        elif date == dt.datetime (2020,6,18):
            return None        
        #these are a few dates where the urls were weird
        elif date == dt.datetime (2020,6,14):
            url="https://coronavirus.dc.gov/release/coronavirus-data-sunday-June-14"
            return url
        elif date == dt.datetime(2020,12,2):
            url="https://coronavirus.dc.gov/release/coronavirus-data-December-2-2020-0"
            return url
        elif date == dt.datetime(2020,12,25):
            url="https://coronavirus.dc.gov/release/coronavirus-data-December-25-2020-december-26-2020"
            return url
        elif date == dt.datetime(2020,12,26):
            if dt.datetime(2020,12,25) in daterange:
                return None
            else:
                url="https://coronavirus.dc.gov/release/coronavirus-data-December-25-2020-december-26-2020"
                return url
        elif date in [dt.datetime(2020,11,14),dt.datetime(2020,11,15),dt.datetime(2020,11,16)]:
            return None
        else:
            url="https://coronavirus.dc.gov/release/coronavirus-data-"+date.strftime("%B-%-d-%Y")
            return url
    for date in daterange:
        url=deathurl(date)
        if url == None:
            if date == dt.datetime(2020,12,26):
                pass
            elif date < dt.datetime(2020,3,20):
                pass
            else:
                deaths=deaths.append(problem_page_data.loc[problem_page_data.date==date])
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
                    newline["sex"]=y[1]
                    newline["url"]=url
                    deaths=deaths.append(newline, ignore_index=True)
            else:
                pass
            time.sleep(3)
            
deathdata("3/03/20","3/28/22")
#fixing one line of text captured
deaths=deaths[deaths["age"]!="Tragically,"]

deaths["date"]=pd.to_datetime(deaths.date)
deaths["age"]=deaths.age.astype(int)

deaths.to_csv("output.csv")