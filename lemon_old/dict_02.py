import re

# d = {0:'了解',re.compile('[a-z]'):'ff'}

# print(d['a'])
d = {('w',22):[34234,5435,534],(11,34):[43543,657657]}


# for i in d:
#     for j in i:
#         print(j)
print(next(iter(d)))

for i in d:
    print(i)