import re


file = open('text_01.txt','r')
txt = file.read()


# res5 = re.sub(r'\((.+);(.+);(.+)\)',r'(\1,\2,\3)',txt)
# print(res1)

# res1 = re.sub(r"'(.+)--(.+)--(.+)'",r"'\1:\2:\3'",res5)
#
# res2 = re.sub(r'--(.+)',r'',res1)
#
# res3 = re.sub(r'PROMPT(.+)',r'',res2)
# res4 = re.sub(r"'(.+);(.+);(.+)';",r"'\1,\2,\3'",res3)
# res4 = re.sub(r"((.+);(.+))",r"\1\2",res3)


# res5 = re.sub(r'(.+);(.+)',r'\1,\2',res3)

res5 = re.sub(r'\((.+);(.+);(.+)\)',r'(\1,\2,\3)',txt)

lis = res5.split(';')

print(res5)
# for l in lis:
#     print('------')
#     print(l)



