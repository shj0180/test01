#!/usr/bin/python
import re


# list=['1','2','index_id(id)(dgdgsd)']



# str = list[2]
# print(str)
#
# par = r".+?(.+?)"
#
# result=re.match(par,str)
# print(result)
# r=result.groups()
# print(r)

# import re
#
# string = list[-1]
# p1 = re.compile(r'[(](.*?)[)]', re.S)  # 最小匹配
# p2 = re.compile(r'[(](.*)[)]', re.S)  # 贪婪匹配
#
# print(re.findall(p1, string))
# print(re.findall(p2, string))
#
# re.S



# line = "Cats are smarter than dogs"
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
#
# str = 'alter table film add cloumn year varchar10'
# p = re.compile('..',re.I)
# result = re.findall(p,str)
# print(result)



#re_simple_match.py


# 过滤sql头部多余的内容
pattern = 'alter'
alltext = '--dsjfhsd\nALTER table modify clo  var();\ncreate table film;'
print(alltext.split(';'))
sql=alltext.split(';')
patterns=['alter','create']
for s in sql:
    sa='%s;'%s
    # print('sa:%s'%sa)

    for p in patterns:

        for match in re.finditer(p, sa, re.I):
            try:
                s = match.start()
                print('text[s:]:%s' % sa[s:])
            except Exception as e:
                pass
            continue


# match = re.search(pattern, text,re.I|re.M)
#
# s = match.start()
# e = match.end()
#
# print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
#     match.re.pattern, match.string, s, e, text[s:e]))
#
# print(text[10:])
#
# 匹配字符串内最少3位，最多5位数字。即满3位就被匹配出来，满5位后另外匹配。
li = 'sAS6666777888'
p = re.compile('[a-zA-Z0-9_]{3,5}',re.I)
res = re.findall(p,li)
print(res)





