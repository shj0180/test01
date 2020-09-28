import re


file = open('text_01.txt','r')
txt = file.read()
# print(txt)
#
# print(type(txt))
# #
#
#
# st ='sffsf'
# print(type(st))

#
# res = re.sub(r'\((.+);(.+)\)',r'(\1,\2)',txt)
# print(res)

res1 = re.sub(r'\((.+);(.+);(.+)\)',r'(\1,\2,\3)',txt)
# print(res1)

lis = res1.split(';')

print(lis)
for l in lis:
    print('------')
    print(l)



# p = re.compile('\(;\)',re.I)
#
# res = re.findall(p,txt)
#
# print(res)

