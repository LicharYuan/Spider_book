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
#add headers信息
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers={'User-agent':user_agent}#对请求头headers处理
r=requests.get('http://www.baidu.com',headers=headers)
print('Agent:'+'\n')
print(r.content)

#响应码

if r.status_code==requests.codes.ok:
    print(r.status_code) #响应码
    print(r.headers)#响应头
    print(r.headers.get('content-type'))#获取头中某个字段
else:
    r.raise_for_status()

    '''
    结果：
    200
    {'Expires': 'Mon, 08 Jan 2018 06:49:53 GMT', 'BDQID': '0xa6ec602a00053cde', 'Vary': 'Accept-Encoding', 
    'BDPAGETYPE': '1', 'Content-Type': 'text/html; charset=utf-8', 'Server': 'BWS/1.1', 
    'Cache-Control': 'private', 'P3P': 'CP=" OTI DSP COR IVA OUR IND COM "', 
    'Set-Cookie': 'BAIDUID=78DEC3FB36B5BA4DDE910337E42EE241:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; 
    max-age=2147483647; path=/; domain=.baidu.com, BIDUPSID=78DEC3FB36B5BA4DDE910337E42EE241; expires=Thu, 31-Dec-37 23:55:55 GMT; 
    max-age=2147483647; path=/; domain=.baidu.com, PSTM=1515394253; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; 
    domain=.baidu.com, BDSVRTM=0; path=/, BD_HOME=0; path=/, H_PS_PSSID=1446_24566_21113_17001_22073; path=/; domain=.baidu.com', 
    'Cxy_all': 'baidu+40563756a866f3427fc8095b7d95690b', 'Date': 'Mon, 08 Jan 2018 06:50:53 GMT', 'Transfer-Encoding': 'chunked',
     'X-Powered-By': 'HPHP', 'X-UA-Compatible': 'IE=Edge,chrome=1', 'Content-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'BDUSERID': '0'}
    text/html; charset=utf-8

    '''


