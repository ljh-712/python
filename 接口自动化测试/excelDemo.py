print('-------------------准备环境------------------------')
'''
操作excel的库:
xlrd、xlwt、xlutils
'''
# 操作excel表
# 1、请求参数-读
import xlrd
excelDir = '../xxx.xls'
#打开excel文件
workBook = xlrd.open_workbook(excelDir,formatting_info=True) # formatting_info=True保持原文件样式
sheets = workBook.sheet_by_name()  # 查看excel文件的子表
workSheet = workBook.sheet_by_name("xxx") # 取需要执行的sheet

#取出数据  1行6列的数据的body
cellData = workSheet.cell_value(1,6).value
# 然后将cellData传入其他函数...
info = 'pass'
# 2、测试结果写入
#文件不存在--新建excel写入  --xlwt
#文件存在，另写新excel--xlutils
from xlutils.copy import copy
# 拷贝excel表对象，结果应该在新的表里

new_workBook = copy(workBook)
# 取拷贝的excel表的sheet  下标
newSheet = new_workBook.get_sheet(1)
#写入数据
newSheet.write(1,9,info)
new_workBook.save(r'../xx.xls')