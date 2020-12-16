# 列表的方法
# 创建一个列表：
stus = ['张三','李四','王五','孙刘']
# append()
stus.append('亚瑟')  # 将列表的最后添加一个元素
print(stus)
# insert()
stus.insert(0,'安其拉') # 在列表0号位置插入元素
print(stus)
# extend() 使用新的序列扩展当前序列相当于+=
stus.extend(['蒙','韩信'])
print(stus) #['安其拉', '张三', '李四', '王五', '孙刘', '亚瑟', '蒙', '韩信']
# clear()清空序列 只针对可变序列
# stus.clear()
# print(stus)
# pop() # 删除并返回被删除元素
print(stus.pop(2)) # 李四
#remove() 删除指定值的元素
stus.remove('韩信')
print(stus) #['安其拉', '张三', '王五', '孙刘', '亚瑟', '蒙']

#reverse
stus.reverse();
print(stus)

# sort()  # 对列表排序
mylist=list("acdb")
mylist.sort()
print(mylist) #['a', 'b', 'c', 'd']
# 如果需要降序排列 传递reverse=True
mylist.sort(reverse=True)
print(mylist)