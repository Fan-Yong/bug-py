 

from time import sleep
from bs4 import BeautifulSoup
from requests import get
import re

 
result1 =[]


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}
url='https://www.dashengpan.com/detail/5ae6e3782f57e94f70b7733cc3c36ce2&keyword=中国古代文学考研'

cookie="upidhhhhfgp=996782469; upidhhhhuuxx=12; upidhhhhudd=18627%2C2; upidhhhhnrfr=1; upidhhhhuuxs=1298; upidhhhhph=7a4f3e45_1; UM_distinctid=176b77f366e399-0426a9581bd099-61141c7d-fa000-176b77f366f30f; dashengpan:sessid=1f681c11-2782-4825-ae99-3c95f9b909e0; dashengpan:sessid.sig=7O84cI3JUMjGmvuPvW5dhoFyBzk; upidhhhhudd=18627%2C2; upidhhhhfgp=996782469; 3544_2368_115.230.65.217=1; 3544_2471_115.230.65.217=1; 3544_2444_115.230.65.217=1; 3544_2448_115.230.65.217=1; 3544_2460_115.230.65.217=1; 3544_2325_115.230.65.217=1; 3544_2319_115.230.65.217=1; 3544_2454_115.230.65.217=1; 3544_2504_115.230.65.217=1; 3544_2444_60.184.184.247=1; 3544_2444_115.226.146.178=1; 3544_2504_27.187.115.19=1; 3544_2454_27.187.115.19=1; 3544_2325_27.156.192.97=1; 3544_2444_220.161.243.76=1; 3544_2325_220.161.243.76=1; 3544_2368_220.161.243.76=1; 3544_2471_27.187.115.19=1; 3544_2325_27.187.115.19=1; 3544_2368_27.187.115.19=1; 3544_2460_27.187.115.19=1; CNZZDATA1279445337=1346168750-1609391403-%7C1609676765; 3544_2444_220.161.199.242=1; 3544_2448_220.161.199.242=1; CNZZDATA1279553784=1771128996-1609392943-%7C1609679528; 3544_2319_220.161.199.242=1; Hm_lvt_76c9f7dc7c9320b3817f6aa42c619ae3=1609673571,1609673966,1609680191,1609681116; Hm_lpvt_76c9f7dc7c9320b3817f6aa42c619ae3=1609681116; richviews_3544=pYaKi1e9ADtVDkTnsvX3WFEu4ySCDGbZrdgbBe6P9hGcPiWzjVgaCmY34f0sCVeksXnAxbHUu9W1mLFNmqDTEyqNvT2hydfyGgTqqk%252B80tMffeo%252FriRqpxxNwgtW9i4JcUC0IkiQhBwpAxVzqX0phzf%252Bnz0A2mC%252ByEDBqEBiQqIXPxyZMVmIpXOvGdM5MwDY%252B03XRaCu%252FEfP9wRhMkP%252Fi8wSXTWyhWrn9Dz%252B500%252B5oYYv%252FRGZpHFhVoHbqRVL3eyNhJymyNlE7Pj3u1uaJPg42T2GB2HaCKLkqYvbKSmQNkcPo49CUHBpQdTOGBcnkcanU7oVcSsXgeyjvQXCrhJJr8dXZmzCrpHNcpWRydvQs596TPbJLycb0b4ugEWFGdm6iCzsY8%252BAGd3g8YdwPPliebBzeH5Ph%252BlWuVal6dadE0Z%252Bm%252BCmBGpGG%252BYqlbKU3Ra5nRIpUa%252FGbLNX%252FRj0XsVxgwlVUudZEr7JgpC2D6GkCquo61apKDZtNu0ii2C80Ije%252FATn2ldIyQwMATmlwFlyJpLScJBysjk7tvFMMnz1q2URdldvHsepRXcOw1Jr99OB700TNRUvOgEYJjFR5TvFkcVK0tFKFjl7i0O9s2lqGBz4%252FYA3TzkD3myjQ1p8k7LUKwNOtnaWsPII31nT8oinWLW%252Fxk7gjHeciUFPCc76qI%253D; 3544_2460_27.156.199.62=1; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg3LjAuNDI4MC44OCBTYWZhcmkvNTM3LjM2"
cookies={}#初始化cookies字典变量 
for line in cookie.split(';'):  #按照字符：进行划分读取 
  #其设置为1就会把字符串拆分成2份 
  name,value=line.strip().split('=') 
  cookies[name]=value #为字典cookies添加内容

response = get(url,timeout=15,headers = headers,cookies=cookies)
trynum=1
#while  (response.status_code ==404 and  trynum<5) :
print("wait......."+url)
while  (response.status_code ==404 ) :
    print("wait............................."+url)
    sleep(3)
    response = get(url,timeout=15,headers = headers)
    #trynum=trynum+1
    

#print (response.status_code)    
response.encoding = 'utf-8'
response.raise_for_status();    
Soup = BeautifulSoup(response.text, 'html.parser')

html=str(Soup.contents[2]) 

html=html.replace('\n','')
html=html.replace(' ','')

#print (Soup.contents)

sourceurl=re.findall(r'button-wrap.*?<a.*?href=.*?http.*?//(.*?)\"',html)    
title=re.findall(r'filename.*?\>(.*?)\<\/h1\>',html)     
size=re.findall(r'文件大小：\<\/span\>(.*?)\<\/span\>',html) 
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
 


print ("----------------the end--------------------------")

# 


     






 
