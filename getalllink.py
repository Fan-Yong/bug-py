############################################
#作用：得到大圣盘某个关键词的所有链接
#by fanyong 20210102
###########################################
import pymysql

from get_level1_link import *

keyword='中国古代文学考研'
#keyword='鼻窦炎'
alllinks=[]
page=1

links=get_level1_link(keyword,str(page))

while (len(links[1])!=0 ):    
    alllinks=alllinks+links[1]
    page=page+1
    next=links[2]
    print( "********"+str(len(links[1]))+"**********")
    print( "********"+str(next)+"**********")
    if(next!=0):
        sleep(2)
        links=get_level1_link(keyword,str(page))
    else:
        break 
    links=get_level1_link(keyword,str(page))
   

conn = pymysql.connect(host="3 ", user=" ",password=" ",database="movie")
cursor = conn.cursor()

for link in alllinks:
    try:
        sql="insert into movie.dsp (keyword_id,url) values (1,'"+link+"')"
        
        cursor.execute(sql)            
        conn.commit()
    except: 
        print("errorrow(dberror):"+sql)
        continue
    
    print ('https://www.dashengpan.com/detail/'+link+'?keyword='+keyword)
    
  

  
