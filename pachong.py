#coding=utf-8
import requests
import json
from lxml import html
#url='https://v1.hitokoto.cn/?c=d&c=e&encode=json' #需要爬数据的网址
url='https://v1.hitokoto.cn/?encode=json' #需要爬数据的网址
page=requests.Session().get(url) 
tree=html.fromstring(page.text) 
#result=tree.xpath('text()') #获取需要的数据
json_str=json.dumps(page.text)
#for i in range(1,20):
data2 = json.loads(json_str)
#print(data2[])
#result=tree.xpath('')
#print(page.json)


#s = json.dumps(page.json)
#print (s)
data=open("data.txt",'w+',encoding='utf-8') 
#print('这是个测试',file=data)
print(data2)
#loads:把json转换为dict
N =10000
for i in range(1,N):
  try:
    #url='https://v1.hitokoto.cn/?c=d&encode=json' #需要爬数据的网址
    page=requests.Session().get(url) 
    #tree=html.fromstring(page.text) 
    s1 = json.loads(page.text)
    
    #打印statusCode对应的值
    ss= str(s1['hitokoto'] )
    s2= str(s1['from'])
    s3= str(s1['from_who'])
    s3=s3.strip().replace('\n', '').replace('\t', '').replace('\r', '').strip()
    ss=ss.strip().replace('\n', '').replace('\t', '').replace('\r', '').strip()
    s2=s2.strip().replace('\n', '').replace('\t', '').replace('\r', '').strip()
    #ss.strip().replace('\r', 'xxxabc')
    #ss.replace('\n', '').replace(’\r’, ‘’)
    #s2.replace('\r', '')
    
    #rstrip(ss)
    #rstrip(s2)
    if (s3 == 'None'):
      tmp = ss + "『" + s2  +"』"
    else:
      tmp = ss + "『" + s2 + "-" +s3 +"』"
    
    print(i,"/",N," ",tmp)
    print(tmp,file=data)
    #print("--[",file=data)
    #print(s1['creator'],file=data)
    #print("]",file=data)
    #print("\n",file=data)
  except:
    print("error!")

#sss="1 1 1\r\n"
#sss=sss.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').strip()
#print(sss,file=data)
