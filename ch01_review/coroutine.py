# a  example for gevent
from gevent import monkey;monkey.patch_all()
import gevent
from urllib import request

def run_task(url):
    print('Visit --> %s' %url)
    try:
        response=request.urlopen(url)
        data=response.read()
        print('%d bytes received from %s.'%(len(data),url))
    except Exception as e: #python2.x:  except Exception,e:
        print(e)
if __name__ == '__main__':
    urls=['https://github.com/','http://www/python.org','http://www.cnblogs.com/']
    greenlets=[gevent.spawn(run_task,url) for url in urls]
    gevent.joinall(greenlets)

'''
Result:
Visit --> https://github.com/
Visit --> http://www/python.org
Visit --> http://www.cnblogs.com/
<urlopen error [Errno -2] Name or service not known>
45571 bytes received from http://www.cnblogs.com/.
51483 bytes received from https://github.com/.

'''