@[TOC](目录)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201018215629841.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTUyMzMx,size_16,color_FFFFFF,t_70#pic_center)

# 安装对应的库
```python
pip install  Mysqlclient
```
# 连接数据库
```python
import MySQLdb

con = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    db='mybatis',
    charset='utf8'

)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/202010182157274.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTUyMzMx,size_16,color_FFFFFF,t_70#pic_center)

# 设置游标对象
```python
c = con.cursor()  
# 游标对象,相当于一个指针，指向数据库第一行数据，依次往下划
```

# 写SQL
## 查询
```python
c.execute('select  * from user')
r = c.fetchone()
print(r) #输出表里第一行数据
r = c.fetchone()
print(r) #输出表里第二行数据


for i in range(c.rowcount): # c.rowcount代表表里的数据条数
    r = c.fetchone()
    if r[1] == '张三':
        print('通过')
        break
```
## 插入(增删改需要提交事务)
```python
# 插入10条数据
for i in range(10):
    c.execute(f"insert into user values({i + 4},'鹿鸣{i + 1}','123456')") 
     # f代表字符串格式化写法

con.commit()
con.close()

```
## 读取Excel数据，并插入到MySQL数据库
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201019121202554.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTUyMzMx,size_16,color_FFFFFF,t_70#pic_center)

```python
import MySQLdb
import pandas as pd
import xlrd
filePath = 'D:\桌面新建文件夹\作业\data.xlsx'
data = pd.read_excel(filePath)
con = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    db='mybatis',
    charset='utf8'

)

c = con.cursor()  # 游标对象
query = "insert into user values(%s,%s,%s)"
for r in range(0, len(data)):
    i = data.iloc[r, 0]
    username = data.iloc[r, 1]
    password = data.iloc[r, 2]
    values = (int(i), str(username), str(password))
    c.execute(query, values)

con.commit()
con.close()
```