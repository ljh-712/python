# 字典 dict
d = {}
print(d)
# 字典的key键可以是任意的不可变对象
# 字典的值可以是任意对象
d = {'name': '孙悟空', 'age': '18'}
print(d)
# 使用函数dict()来创建
d = dict(name='ls', age=18)
print(d)
# 也可以将一个双值子序列转化为字典
# 双值子序列 [1,2] ('a',3) 'ab'
d = dict([('name', 'wudu'), ('s', 'd')])  # {'name': 'wudu', 's': 'd'}
print(d)
# in    not in 检查字典中是否包含指定的键

# 获取字典中的值，通过值获取键
print(d['name'])  # 通过[]通过键获取值，如果键不存在会抛出KeyError异常
print(d.get('name'))  # 通过get()通过键获取值，如果键不存在会返回None
# 也可以指定一个默认值
print(d.get('hello', '默认值'))  # 如果hello键不存在会返回默认值

# 修改字典d[key]=value，如果key存在则覆盖，不存在则添加
d['name'] = 'zhang'
print(d)  # {'name': 'zhang', 's': 'd'}
# 如果字典中不存在该key会自动将该键值对添加至字典中
d['address'] = 'huaguoshan'
print(d)  # {'name': 'zhang', 's': 'd', 'address': 'huaguoshan'}
r=d.setdefault('name','猪八戒')  # 如果key已存在于字典中，则返回key的值，不会对字典做任何操作,没有就添加
print(r) # zhang
print(d) # {'name': 'zhang', 's': 'd', 'address': 'huaguoshan'}

# update([other])
#将其他字典的key-value添加到当前字典中,如果有重复的key,后面的key的value会替换前面的
d={'a':1,'b':2,'c':3}
d1={'d':1,'e':2,'f':3}
d.update(d1)
print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3}

# 删除字典 del
del d['a']
print(d) # {'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3}
# popitem() 一般删除最后一个键值对  删除后会将删除的key-value作为返回值，返回的是有两个元素的元组
r=d.popitem()
print(r) # ('f', 3)
print(d) # {'b': 2, 'c': 3, 'd': 1, 'e': 2}
# pop()根据key删除key value，并返回删除key的值
r=d.pop('c')
print(r) # 3
print(d) # {'b': 2, 'd': 1, 'e': 2}
# r =d.pop('g') # KeyError: 'g'，报错，因为key不存在
print(d)
r1=d.pop('g','默认值') # 但是如果指定了默认值，再删除不存在的key,不会报错而是直接返回默认值
print(r1)
print(d)
# clear()清空字典

# copy()该方法对字典进行浅复制（只复制对象里的值）
# 复制以后的对象，和原对象是独立的，修改一个不会影响另一个
d={'a': 1, 'b': 2, 'c': 3}
d1=d.copy()
print(d1) # {'a': 1, 'b': 2, 'c': 3}
# 浅复制（只复制对象里的值），如果值也是一个可变对象，那么这个可变对象不会被复制
d2={'a':{'name':'孙悟空','age':18},'b':1}
d3=d2.copy()
print(d2) # {'a': {'name': '孙悟空', 'age': 18}, 'b': 1}
print(d3) # {'a': {'name': '孙悟空', 'age': 18}, 'b': 1}
d3['a']['name'] = '猪八戒'
print(d2) # {'a': {'name': '猪八戒', 'age': 18}, 'b': 1}
print(d3) # {'a': {'name': '猪八戒', 'age': 18}, 'b': 1}

# 字典遍历
# keys() 返回字典所有的key
print(d.keys()) # dict_keys(['a', 'b', 'c'])
for k in d.keys():
    print(d.get(k))
# values()  返回字典所有的value
for v in d.values():
    print(v)
# items()  返回一个序列，双值分别是字典做的key-value
print(d.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)])
for k,v in d.items():
    print(k,'=',v)