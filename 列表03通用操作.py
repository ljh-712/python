# + 和 *
mylist = [1,2,3] + [4,5,6]
print(mylist)
mylist = [4,5,6] * 3
print(mylist)

# 创建一个列表：
stus = ['张三','李四','王五','孙刘']

# not in 和 in
# max() 和 min()

# index() 和 count() 是方法
# xxx.方法  方法必须通过对象调用，

# s.index()  获取元素在指定列表中的第一次出现时索引
print(stus.index('张三'))
stus1 = ['张三','李四','王五','孙刘','李四','李四']
print(stus1.index('李四',2)) # index第二个参数表示查找的起始位置
print(stus1.index('李四',2,5)) # 第三个参数表示查找结束的位置，包括开始不包括结束

# s.count()  统计指定元素在列表中出现的次数
print(stus1.count('李四'))