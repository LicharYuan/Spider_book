#编码JSON，解码例子

import json
str=[{"username":"lichar","age":"21"},(2,3),1]
json_str=json.dumps(str,ensure_ascii=False)
print(json_str)
with open('lichar.json','w') as fp:#lichar.txt as the same
    json.dump(str,fp=fp,ensure_ascii=False)
    '''
    打印结果：
    [{"age": "21", "username": "lichar"}, [2, 3], 1]

    '''
#dump/dumps是一个json编码方法
#dump把Python对象转换成JSON对象，通过fp文件流写入；
# dumps则是生成一个字符串

#load/loads是json解码方法
#区别同上

new_str=json.loads(json_str)
print(new_str)
with open('seputu.json','r') as fp:
    for loads in json.load(fp):
        print(loads)
        print('\n')

    '''
    此段：
    [{'username': 'lichar', 'age': '21'}, [2, 3], 1]
    [{'username': 'lichar', 'age': '21'}, [2, 3], 1]

    '''

#也可以操作后缀为txt的文件
