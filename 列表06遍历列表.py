# 遍历列表就是将列表中元素的值取出来
# 创建一个列表：
stus = ['张三','李四','王五','孙刘']

# 创建一个while循环
i=0
while i< len(stus):
    print(stus[i])
    i+=1

# 通过for循环
# 语法：for 变量 in 序列:
#      代码块
for s in stus:
    print(s)