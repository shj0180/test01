import xlrd

# import xlutils
# from xlutils import copy

# 读取
exceldir = '/Users/shihuajun/Documents/生活/demo.xls'
workbook = xlrd.open_workbook(exceldir)

print(workbook.sheet_names())
ws = workbook.sheet_by_index(0)
data = {}
print(ws.nrows)
headers = []
for row in range(ws.nrows):
    if row == 0:
        continue
    elif row==1:
        headers = ws.row_values(row)
    else:
        data.setdefault(row,dict(zip(headers,ws.row_values(row))))
print(data)

# worksheet = workbook.sheet_by_name('shangqi')
#
# # 读取一行
# rows = worksheet.row_values(9)
# print(rows)
#
# # 读取一列
# col = worksheet.col_values(0)
# print(col)
#
# # 读取指定坐标单元格里的值
# cell = worksheet.cell_value(9,1)
# print(cell)
#
# # 单元数据类型
# celltype = worksheet.cell(9,1).ctype
# print(celltype)















