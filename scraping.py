# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:15:55 2021

@author: chunr
"""

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
      
    height = 0
    status = True
    error = 0
    while status:
        time.sleep(2)
        try:
            new_height = driver.find_element_by_xpath('//div[starts-with(@style,"position: relative;")]').size['height']
        except: 
            driver.get("https://twitter.com/search?q=(from%3A"+company+")%20until%3A"+str(year)+"-"+str(month)+"-"+str(day+1)+"%20since%3A"+str(year)+"-"+str(month)+"-"+str(day)+" -filter%3Areplies&src=typed_query")
            error = error + 1 
            if error == 10:
                break
            continue
    # 每执行一次滚动条拖到最后，就进行一次参数校验，并且刷新页面高度
        if new_height > height:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            height = new_height
            time.sleep(2)
        else:
        # 当页面高度不再增加的时候，我们就认为已经是页面最底部，结束条件判断
            print("滚动条已经处于页面最下方!")
            print(height)
            driver.execute_script('window.scrollTo(0, 0)')  # 把滚动条拖到页面顶部
            break
    if error == 10:
        continue

    qian = (driver.find_element_by_xpath('//div[starts-with(@style,"position: relative;")]').text).split("·",1)[0]
    height_reference_flag = True 
    last = 0 
    flag = 0
    reference_url = []
    target = 0 
    while height_reference_flag: 
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,1500)")
        time.sleep(1)
        total_text =  driver.find_element_by_xpath('//div[starts-with(@style,"position: relative;")]').text  
        time.sleep(2)
        try:
            url_list = [i.get_attribute('href') for i in driver.find_elements_by_xpath('//*[starts-with(@href,"/'+company+'/status/")]') ]
        except: 
            time.sleep(60)
            url_list = [i.get_attribute('href') for i in driver.find_elements_by_xpath('//*[starts-with(@href,"/'+company+'/status/")]') ]
        if url_list == reference_url:
            height_reference_flag = False 
            break
        new_url_list = []
        for i in url_list:
            if i[-2:] in ['/1','/2','/3''/4','/5','/6']:
                continue
            else:
                new_url_list.append(i)
        data_url["url"] = data_url["url"]+ new_url_list
        s_text = total_text.split(qian+'·\n')[1:]
        reference_url = url_list
        for i in s_text:
            info  = i.split("\n",1)
            if len(info)>1:
                data_info["date"].append(info[0])
                data_info["twit"].append(info[1])
            else:
                data_info["date"].append(info[0])
                data_info["twit"].append(info[0])
    

data_info = pd.DataFrame(data_info).drop_duplicates() 
data_info.sort_values("twit",inplace=True)  
data_url = pd.DataFrame(data_url).drop_duplicates() 

date_list = []
twit_list = []
date = data_info["date"].tolist()
twit = data_info["twit"].tolist()
reference_date = ''
reference_twit = ''
for i,j in zip(date,twit):
    if reference_date == i:
        if (len(reference_twit)+1 == len(j)) and j[-1] =='\n':
            continue 
    date_list.append(i)
    twit_list.append(j)
    reference_date = i
    reference_twit = j


            
            
    
data_info = {'date':date_list,'twit':twit_list}
pd.DataFrame(data_info).to_excel(company+".xlsx")
pd.DataFrame(data_url).to_excel(company+"_url.xlsx")
