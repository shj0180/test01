import csv
path = '../../data/one.csv'
headers = ['name','age','class','high','money']
list =  [['孙悟空',600,'花果山',2.3,2000],['猪八戒',400,'高老庄',2.2,1500],['沙和尚',380,'流沙河',2.2,1400]]


with open(path,'wt',encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    for i in list:
        f_csv.writerow(i)







