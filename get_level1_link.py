############################################
#作用：得到大圣盘某个关键词某页的所有链接
#by fanyong 20210102
###########################################


from time import sleep
from bs4 import BeautifulSoup
from requests import get
import re

#print (get_level1_link('中国古代文学考研','1'))
#keyword='中国古代文学考研'
#page=1



def get_level1_link(keyword, page):

    titles=[]
    links=[]
    
    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}
    url='https://www.dashengpan.com/s?kw='+keyword+"&page="+page
    
    response = get(url,timeout=15,headers = headers)
    trynum=1
    #while  (response.status_code ==404 and  trynum<5) :
    print("wait......."+url)
    while  (response.status_code ==404 ) :
        print("wait............................."+url)
        sleep(3)
        response = get(url,timeout=15,headers = headers)
        #trynum=trynum+1
        
    if  trynum==5:
         #0:timeout   
         return (0,[],0)    
    #print (response.status_code)    
    response.encoding = 'utf-8'
    response.raise_for_status();    
    Soup = BeautifulSoup(response.text, 'html.parser')
    
    
     
     
    h1s_p=Soup.find_all(name='h1',class_='resource-title')
    
    for h1_p in h1s_p:     
        titles.append(h1_p.text.strip())
    
    con=''.join( str(ii) for ii in Soup.contents[2])
    #print(con)
    #print("-====================================================")
    
    
    links=re.findall(r'res\=\{id\:\"(.*?)\"',con)
    
    #for index ,v in enumerate(links):
    #print ( titles[index]+":"+links[index])
    #print(len(links))
    #print(len(titles))
    next=0;
    if(con.find('下一页')!=-1):
        next=1
    
    #1:是否超时，3：是否有下一页
    return (1,links,next)
     






 
