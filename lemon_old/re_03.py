import re
# for i in range(1,5):
#     y = 4
#     if y == i:
#         break
#     else:
#         print(i)


# res=input("anything:")

# print(type(res))

str = 'create table ggu'

# print(type(str))

pat = re.compile('create table (.+)',re.I)

m = pat.match(str)
t = m.group()

print(t)

