# 可变对象：指数据的值value可以改变
# 每个对象里都保存了三个数据：id(标识)、type(类型)、value(值)

a = [1, 2, 3]
# 通过索引修改列表
a[0] = 10  # 该操作是通过变量去修改对象的值，不会改变变量所指向的对象

# 为变量重新赋值
a = [4, 5, 6]  # 改变变量所指向的对象

# 为一个变量重新赋值时不会影响其他变量

# ==    !=    is    is not
# == 比较两个对象的值(value)是否相等
# is 比较两个对象id是否相等
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
