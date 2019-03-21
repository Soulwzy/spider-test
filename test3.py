import csv
# Windows默认编码是gbk，如果用utf-8，excel打开可能会乱码
# newline='' 是为了让writer自动添加的换行符和文件的不重复，防止出现跳行的情况
file_obj = open('csvtest.csv', 'w', encoding="gbk", newline='')
writer = csv.writer(file_obj)
a_row = ['你好', 'hello', 'thank', 'you']
row_2 = ['how', 'are', 'you', 'indian', 'mifans']
writer.writerow(a_row)
writer.writerow(row_2)
file_obj.close()
print('finished!')