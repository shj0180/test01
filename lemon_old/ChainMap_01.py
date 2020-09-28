from collections import ChainMap
# ChainMap 使用原来的字典，它自己不创建新的字典。
# update() 方法创建一个完全不同的字典对象（或者是破坏现有字典结构）。 同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去
a = {'x': [1,2,55], 'z': 3 }
b = {'y': 2, 'z': 4 }

c= ChainMap(a,b)
# print(c.keys())
#
# print(c['x'])
# print(c['z'])

for i in a:
    print(a[i][2])


