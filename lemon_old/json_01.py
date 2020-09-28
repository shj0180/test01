#coding=utf-8

import json


dict = {'师傅':'唐僧','大徒弟':'孙悟空','二徒弟':'猪八戒','三师弟':'沙和尚'}
# dict = {'a':1,'b':33,'df':'fgsd'}

# dict---> str
ret = json.dumps(dict)
print(ret,type(ret))

# 将中文正常打印
ret2 = json.dumps(dict,ensure_ascii=False)
print(ret2)

# str --encode--> 字节
byte_8 = ret.encode('utf-8')
print(byte_8)


# 字节 --decode--> str
str8 = byte_8.decode('utf-8')

# str  --json.loads-->dict
res_json = json.loads(str8)
print(res_json,type(res_json))


with open('西游记.txt',mode='w',encoding='utf-8') as f:
    # f.write(json.dumps(dict))
    f.write(ret2)

with open('西游记.txt',encoding='utf-8') as fil:
    str1= fil.read()
    print(str1)

    dict2 = json.loads(str1)
    print(dict2)

# key 必须是字符串，value只能是 ： 字典、列表、字符串、数字、布尔值
# 才能将dict转成json格式的str，这样就能传给java


str4 = json.dumps(['dd',44])
print(str4,type(str4))


dict3 = json.loads(str4)
print(dict3,type(dict3))
print('***************')


# ******************************************************
# dump、load 是可以直接和文件句柄发生交互
with open('s_55_dumptest.txt','w',encoding='utf-8') as f:
    json.dump(dict,f,ensure_ascii=False)

# 将文件中的json格式的字符串读取，按dict
with open('s_55_dumptest.txt',encoding='utf-8') as f:
    res =json.load(f)
print(res,type(res))



#
# luo = "{'s':[2,3],'ff':44}"
# dlis = json.loads(luo)
# print(dlis,type(dlis))

luo1 = '{"s":[2,3],"ff":44}'
dlis1 = json.loads(luo1)
print(dlis1,type(dlis1))















