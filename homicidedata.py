#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:00:13 2021

@author: danielstone
"""


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

global deaths
deaths=pd.DataFrame()

for x in range(1,2000):
    baseurl="http://dc-witness.herokuapp.com/viz/"
    number=str(x)
    url=baseurl+number
    try:
        req = requests.get(url)
        soup=BeautifulSoup(req.text, "lxml")
        newline={}
        newline["age"]=int(soup.select("p.factoid.full-name-and-age")[0].text.split(",")[1].strip())
        newline["name"]=soup.select("p.factoid.full-name-and-age")[0].text.split(",")[0]
        newline["gender"]=soup.select("p.factoid.demographics")[0].text.strip()
        newline["year"]=int(soup.select("div.col.date")[0].text.strip().split()[3].replace("'",str(20)))
        newline["month"]=soup.select("div.col.date")[0].text.strip().split()[1]
        newline["day"]=int(soup.select("div.col.date")[0].text.strip().split()[2].replace(",",""))
        newline["how"]=soup.select("div.col.left-most.how")[0].text.strip()
        newline["url"]=url
        deaths=deaths.append(newline, ignore_index=True)
        print(url)
    except:
        print("NO DATA AT "+url)
        pass

deaths["month"]=deaths.month.replace(['Jan.', 'Feb.', 'Oct.', 'Mar.', 'May.', 'Nov.', 'Aug.', 'Apr.',
       'Sep.', 'Jul.', 'Jun.', 'Dec.'],[1,2,10,3,5,11,8,4,9,7,6,12])

deaths.to_csv("dchomicides.csv")
    
    
    

