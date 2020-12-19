# fileName = 'test.txt'
# # 文件读取
# # fileObj = open(fileName)  # 打开文件
# # content = fileObj.read()  # 读取文件
# # print(content)
# # fileObj.close()  # 关闭文件
#
# # with ... as操作文件可以自动关闭
# # read()可以接受一个size作为参数
# try:
#     with open(fileName, encoding='utf-8') as fileObj:
#
#         # 定义一个变量，指定每次读取的大小
#         chunk = 4
#         while True:
#             # 读取chunk大小的内容
#             content = fileObj.read(chunk)
#             # 检查是否读取了内容
#             if not content:
#                 # 内容读取完毕，退出循环
#                 break
#             print(content, end='')  # end表示取消换行
# except FileNotFoundError:
#     print(f'{fileName}不存在')
#
# # fileObj.readline() 读取一行内容
# # fileObj.readlines() 一行一行读取内容，会一次性将读取到的内容封装到一个列表返回
#
#
# # 文件写入
# with open(fileName, mode='w', encoding='utf-8') as file_obj:
#     file_obj.write("悯农\n")
#     file_obj.write("作者：李白")
#     # 使用write如果文件不存在，就会创建文件，如果存在就覆盖原文件


# 读二进制文件
# t代表文本文件
# b代表二进制文件
file_name="D:/Picture/t.jpg"
with open(file_name,'rb') as file_obj:
    # print(file_obj.read(100))
    # 将读取的文件写入
    new_name='t1.jpg'
    with open(new_name,'wb') as new_obj:
        chunk=1024*100
        while True:
            content=file_obj.read(chunk)
            if not content:
                break
            new_obj.write(content)
