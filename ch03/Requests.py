import requests
import chardet
r=requests.get('http://www.baidu.com')
# print(r.content)
print(chardet.detect(r.content))
#结果 ----->{'language': '', 'encoding': 'utf-8', 'confidence': 0.99}
print('text---->'+r.text)
print('encoding---->'+r.encoding)
r.encoding='utf-8'
print('new text---->'+r.text)

#以上是全部响应的模式
#还有一种流模式
r_2=requests.get('http://www.baidu.com',stream=True)
print(r_2.raw.read(10))#r.raw.read()指定读取的字节数

user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers={'User-agent':user_agent}#对请求头headers处理
r=requests.get('http://www.baidu.com',headers=headers)
print('Agent:'+'\n')
print(r.content)