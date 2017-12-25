from urllib import request
import urllib.parse as parse
url='https://weibo.com'

postdata={'username':'541277881@qq.com',
          'password':'ylc19970310' }
data=parse.urlencode(postdata).encode(encoding='UTF8')
#之前有报错 -> TypeError: POST data should be bytes or an iterable of bytes. It cannot be of type str.
#加入.encode(……)
req=request.Request(url,data)
response=request.urlopen(req)
html=response.read()
print(len(html))
