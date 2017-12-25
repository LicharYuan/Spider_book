from urllib import request
response=request.urlopen('https://weibo.com')
html=response.read()
print(html)