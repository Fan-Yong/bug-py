# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:32:16 2021

@author: Administrator
"""

import pymysql
import re

result1 =[]
 

conn = pymysql.connect(host=" ", user=" ",password=" ",database=" ")
cursor = conn.cursor()

sql="SELECT url,html FROM bug_html     order by id asc" 
ret=cursor.execute(sql)
data = cursor.fetchall()

for row in data:
    html=row[1]
    html=html.replace('\n','')
    html=html.replace(' ','')
    sourceurl=re.findall(r'button-wrap.*?<a.*?href=.*?http.*?//(.*?)\"',html)    
    title=re.findall(r'filename.*?\>(.*?)\<\/h1\>',html)     
    size=re.findall(r'文件大小.*?span\>(.*?)\<\/span\>',html) 
    updatetime=re.findall(r'更新时间.*?span\>(.*?)\<\/span\>',html) 
    source=re.findall(r'内容来源：(.*?)\<\/span\>',html) 
    list=re.findall(r'detail-item-title.*?\>(.*?)\<\/span\>',html)    
    password=re.findall(r'提取密码\<\/span\>(.*?)\<span',html)
    
    print("".join(sourceurl))
    print("".join(title))
    print("".join(size))
    print("".join(updatetime))
    print("".join(source))
    print("!@!".join(list))
    print("".join(password))
 
    u=(row[0],"".join(title),"".join(sourceurl),"".join(password),"".join(size),"".join(updatetime),"!@!".join(list),"".join(source))
    result1.append(u) 
n=1
for r in result1:
  try:
    sql = "insert into dsp_content (id,dashengpanurl,title,sourceurl,password,szie,updatetime,list,source) values "
    sql=sql+"("+str(n)+",'"+r[0]+"',"
    sql=sql+"'"+r[1]+"',"   
    sql=sql+"'"+r[2]+"',"
    sql=sql+"'"+r[3]+"',"
    sql=sql+"'"+r[4]+"',"
    sql=sql+"'"+r[5]+"',"
    sql=sql+"'"+r[6]+"',"
    sql=sql+"'"+r[7]+"')"
    
    cursor.execute(sql)
    conn.commit()
    n=n+1
  except: 
    print(sql)
    continue
print ("aaa")
      