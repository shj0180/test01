import csv
path= './one.csv'

def read1():
    with open(path,'rt',encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            print(row)

def read2():
    with open(path, 'rt', encoding='utf-8') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            # print(row)
            if row['name'] == '孙悟空':
                print(row)



read1()
read2()
