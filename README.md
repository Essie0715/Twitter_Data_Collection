# Twitter_Data_Collection
Twitter scraping using selenium 


# Setup

##### 1. install Selenium
This repo requires Selenium 3.141.0+, please see [here](https://selenium-python.readthedocs.io/) for installaton instruction.



# Quick Start
```python
import requests
import os 
import pandas as pd 
from selenium import webdriver 
import time 


#Info that you want to collect 
data_info = {'date':[],'twit':[]} #Tweets time tag and content
data_url = {"url":[]} #Tweets URL
company = "LSValue" #User tag 

driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe') #Change path as per required 

#Time line 
year_list = range(2010,2020)
month_list = range(1,13)
for year in year_list:
 for month  in  month_list:
  if month in [1,3,5,7,8,10,12]:
      day_list = range(1,31)
  elif month in [4,6,9,11]:
      day_list = range(1,30)
  else:
      day_list = range(1,28)  
  for day in day_list:
    if day%2==1:
        driver.get("https://twitter.com/search?q=(from%3A"+company+")%20until%3A"+str(year)+"-"+str(month)+"-"+str(day+1)+"%20since%3A"+str(year)+"-"+str(month)+"-"+str(day)+" -filter%3Areplies&src=typed_query")
    else: 
        continue
```
