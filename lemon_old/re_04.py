#coding=utf-8
import re

str="dfdsf UP;DATE ooo.t_fdsf;SET 'No;n;e' dhsf;g_name =  kkk"
# right_dml_list =[]
# def getdml():
#     sql = str[0]
#     print(sql)
#     patterns = ['update (.+?) set (.+?)']
#     for pattern in patterns:
#         for match in re.finditer(pattern,sql,re.I):
#             try:
#                 s=match.start()
#                 print(s)
#                 print(sql[s:])
#                 right_dml_list.append(sql[s:])
#                 print(right_dml_list)
#             except Exception as e:
#                 print(e)
#
# getdml()



# 将str中的none替换成null
# str1=re.sub("'None'",'Null',str)
# print(str1)

str1=re.sub("'((.+;){3}).+'",'???',str)
print(str1)


# # 手机号的匹配
# phonenum = input("输入手机号:")
# # ^ 及 $ 固定开头和尾部，即只匹配这个头部到尾部长度的字符串，不符合该长度就不会匹配。
# # 如果不用这2个符号，那么就会在匹配对象中去寻找，找到就显示
# regex = '^1[2-9]\d{9}$'
# ret = re.findall(regex,phonenum)
# print(ret)


# re.search  从头往后找，任何地方有符合条件的都返回
# re.match  从头开始匹配，如果开始部分匹配到就匹配成功，否则失败

res1 = re.search(r'\d+',r'ale84')
print(res1.group())

res2 = re.match(r'\d+',r'84ale')
print(res2.group())

res3 = re.match(r'\d+',r'ale55')
print(res3)

[22,'ss',['ss'],{3,44}]


stockid = '600000'
res4 = bool(re.match('20',stockid))

print(res4)

pattern = {'sh':['60','900'],'sz':['00','200','300']}
for i in pattern:
    for j in pattern[i]:
        r = bool(re.match(j,stockid))
        print(r)




