name=['唐僧','孙悟空','猪八戒','沙和尚','红孩儿','牛魔王']

from random import randint,sample
from functools import reduce

#随机取样
s1=sample(name,3)
s2=sample(name,3)
s3=sample(name,3)
s4=sample(name,3)

print(s1)

d1={i:randint(0,1000) for i in s1}
d2={i:randint(0,1000) for i in s2}
d3={i:randint(0,1000) for i in s3}
d4={i:randint(0,1000) for i in s4}

print(d1)
print(d2)
print(d3)
print(d4)

# map函数得到所有字典keys集合
print(map(dict.keys, [d1, d2, d3,d4]))
# reduce函数得到所有字典keys的交集
re = reduce(lambda x, y: x & y, map(dict.keys, [d1, d2, d3,d4]))
print(re)



