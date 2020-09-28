import os

# sqlfile_data = input('输入日期:')

def get_path():
    schema_all=('test01','test02')

    for schema in schema_all:
        path ='/Users/shihuajun/Documents/python/20190206/%s/仅测试'%(schema)
        for i in os.listdir(path):
            SqlFile_path = path +'/' +i
            print(SqlFile_path)










