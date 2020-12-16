# 创建一个列表：
stus = ['张三','李四','王五','孙刘']

# 修改序列
# 直接通过索引修改元素
stus[0]='张秒'
print(stus)

# 通过del删除
del stus[0]
print(stus)

# 通过切片修改元素，在给切片赋值时只能使用序列
stus[0:2] = ['主七','崇拜']
print(stus)
stus[0:0]=['王非'] #像索引为0的位置插入元素
print(stus) #['王非', '主七', '崇拜', '孙刘']
# 当设置了步长时，序列中元素个数必须和切片中元素个数一致
stus[::2]=['安其拉','亚瑟']
print(stus) # ['安其拉', '主七', '亚瑟', '孙刘']
stus[1:2]=[]

#以上操作只适用于可变序列
# s="hello" 字符串是个不可变序列
# s[1]='E'
# print(s)  # 'str' object does not support item assignment

# 如果想修改不可变序列，可以通过list()函数将其他序列转化为list;
s='hello'
s=list(s)
s[0]='1'
print(s)
