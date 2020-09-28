from random import randint
name=['唐僧','孙悟空','猪八戒','沙和尚']
d={i:randint(60,1000) for i in name}
print(d)


# print(sorted(d))
#
# print(d.keys())
# print(d.values())
#
# t=sorted(zip(d.values(),d.keys()))
# print(t)



print(d.items())
d.items()

l=sorted(d.items(),key=lambda x:x[1])

print(l)