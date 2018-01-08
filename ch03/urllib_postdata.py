from urllib import request
import urllib.parse as parse
url='https://weibo.com'

postdata={'username':'541277881@qq.com',
          'password':'ylc19970310' }
data=parse.urlencode(postdata).encode(encoding='UTF8')
#之前有报错 -> TypeError: POST data should be bytes or an iterable of bytes. It cannot be of type str.
#加入.encode(……)
req=request.Request(url,data)
try:
    response=request.urlopen(req)
    print(response.getcode())
    html = response.read()
except request.HTTPError as e:
    if hasattr(e,'code'):
        print('Error code',e.code)   #  返回HTTP 响应码

print(len(html))
#add 请求headers info.
#方法一：
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
req.add_header('User-Agent',user_agent)
#方法二：
headers={'User-Agent':user_agent}
req=request.Request(url,data,headers)

#设置proxy
proxy=request.ProxyHandler({'http':'127.0.0.1:8087'})
opener=request.build_opener([proxy,])
request.install_opener(opener)#设置全局的代理
response=request.urlopen(url)
#单个网站使用代理：
opener=request.build_opener(proxy,)
response=opener.open(url)
print(response.read())

#总结：
#要传输数据需要编码
#头信息和数据传输都需要Request
#然后再request.urlopen()


