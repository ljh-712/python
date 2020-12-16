# 元组tuple
# 不可变序列
# 操作基本上和列表一致
# 一般情况希望数据不改变就使用元组，其余都使用列表


# 创建元组
mytuple = ()
print(mytuple)
print(type(mytuple))
mytuple = (1, 2, 3, 4, 5)
print(mytuple)
# 不能为元组中的元素重新赋值

# 如果元组不是空元组，它里边至少有一个,
t = (10,)
print(type(t))

# 元组的解构/解包（将元组中的每一个元素都赋值给一个变量）
tp = 10, 20, 30, 40
a, b, c, d = tp
print('a=', a)  # a= 10
print('b=', b)  # b= 20
print('c=', c)  # c= 30
print('d=', d)  # d= 40

# python交换两个变量的值
a = 100
b = 200
a, b = b, a
print(a, b)

# 对元组解包时，变量数量必须和元组数量一致
k = 10, 20, 3, 4
a, b, *c = k  # 在变量前加个*将会获取元组中所有剩余元素，剩余元素保存到列表
print(a,b) # 10 20
print(c) # [3, 4]
