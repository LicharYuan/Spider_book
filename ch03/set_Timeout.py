from urllib import request
req=request.Request('http://www.zhihu.com')
response=request.urlopen(req,timeout=2)#setting timeout python=3.5*
html=response.read()
print(html)
