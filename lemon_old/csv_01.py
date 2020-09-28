#coding='utf-8'
import os
import csv
path = '/Users/shihuajun/PycharmProjects/2019/test01/lemon_old/s_62_csv.csv'
headers = ['name','age','class','high','money']
#
p1 = [['孙悟空',600,'花果山',2.3,2000],['猪八戒',400,'高老庄',2.2,1500],['沙和尚',380,'流沙河',2.2,1400]]
def create():
    with open(path,'wt',encoding='utf-8') as f:
        f_csv = csv.writer(f,lineterminator = '\n')
        f_csv.writerow(headers)
        for i in p1:
            f_csv.writerow(i)

# create()
l= []
with open(path,'rt',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for row in f_csv:

        print(row)
        l.append(row)
print(l)





















