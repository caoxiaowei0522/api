import xlrd
from xlutils.copy import copy
#先读取Excel
def readExcel(path,sheet_num):
    workbook=xlrd.open_workbook(path)
    worksheet=workbook.sheet_by_index(sheet_num)
    print(worksheet.nrows)
    retlist=[]
    for i in range(1,worksheet.nrows):
        row=worksheet.row_values(i)
        retlist.append(row)
    return  retlist
#复制到新的Excel里
def getnewexcel(filePath):
    workbook = xlrd.open_workbook(filePath, formatting_info=True)
    print(workbook.nsheets)
    newworkbook=copy(workbook)
    return newworkbook