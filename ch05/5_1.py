import json
import requests
from bs4 import BeautifulSoup
user_agent='Mozilla/5.0 (compatible;MSIE 5.5;Window NT)'
headers={'User-Agent':user_agent}
r=requests.get('http://seputu.com/',headers=headers)
# print(r.text)
#获取标题，章节
soup=BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
content=[]
for mulu in soup.find_all(class_="mulu"):
    h2=mulu.find('h2')
    if h2!=None:
        h2_titile=h2.string
        list=[]
        # print(h2_titile)
        for a in mulu.find(class_='box').find_all('a'):#获取所有a的标记中url和章节内容
            href=a.get('href')
            box_title=a.get('title')
            print(href,box_title)
            list.append({'href':href,'box_title':box_title})
        content.append({'title':h2_titile,'content':list})
with open('seputu.json','w') as fp:
    json.dump(content,fp,indent=4).encoding('utf-8')


'''
       出现：UserWarning: You provided Unicode markup but also provided a value for from_encoding. 
            Your from_encoding will be ignored.warnings.warn
            ("You provided Unicode markup but also provided a value for from_encoding. Your from_encoding will be ignored.")
'''
