person_xiyouji ={"师傅":"唐僧","大师兄":"孙悟空","二师兄":"猪八戒","三师弟":"沙和尚","四师弟":"白龙马"}

for i in person_xiyouji:
    print(i)

#
# #取值
# print(person_xiyouji["师傅"])
#
# #删除
# sishidi=person_xiyouji.pop("四师弟")
# print(sishidi)
# print(person_xiyouji)
#
# #增加、修改
# person_xiyouji["小师弟"]="白龙马"
# print(person_xiyouji)
#
# person_xiyouji["小师弟"]="小白龙"
# print(person_xiyouji)
#
# #统计键值对数量
# num=len(person_xiyouji)
# print(num)
#
# #合并字典
# temp={"妖精1":"大鹏鸟"}
# person_xiyouji.update(temp)
# print(person_xiyouji)

#循环---k是key
for k in person_xiyouji:
    print(person_xiyouji[k])
    print("西游记里有%s:%s"%(k,person_xiyouji[k]))

# #多个字典放在一个list里
#
#
# #
# #
# data=[i for i in range(1,4)]
# print(data)
# d=dict.fromkeys(data,data)
# print(d)

# l=[]
# a= (('film',id,'name'),('user',id,'coutry'))
# for i in a:
#     print(i[0])
#     l.append(i[0])
# # print(a[1:3])
# print(l)
# # print(dict(l))
#
# for i in l:
#     if i==l:
#         d=dict.fromkeys(l,i)
#         print(d)

d1 = {'x':'1'}
d2 = {'x':'2'}
k = d1.keys()
print(k)


