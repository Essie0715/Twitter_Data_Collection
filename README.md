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

#Info 
data_info = {'date':[],'twit':[]}
data_url = {"url":[]}
company = "LSValue"
#load the link
#Initialization 
#driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe') 
#Log in 

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

```
