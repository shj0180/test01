from random import randint
data = [randint(-10,10) for _ in range(5)]
print(data)

# t=filter(lambda x: x>=0,data)
# for i in t:
#     print(i)

#list解析
l=[t for t in data if t >=0]
print(l)

#字典解析
dict={x:randint(60,100) for x in range(1,11)}
print(dict)
dict1={k:v for k,v in dict.items() if v>90}
print(dict1)





