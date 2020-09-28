
list1 = ['水电费','是大多数非','大萨达深V']

# 直接生成list，但如果生成的list过大会有性能问题
res1 = [n+'删除' for n in list1]
print('res1：%s'%res1)

# 生成器
res2 = (n+'删除' for n in list1)
print(res2)
for r in res2:
    print(r)

# map
res3 = map(lambda n:n+'删除',list1)
print(res3)
for r3 in res3:
    print(r3)




