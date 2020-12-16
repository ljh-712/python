# range()是一个函数，可以用来生成自然数序列
r=range(5)
print(r)
print(list(r)) #[0, 1, 2, 3, 4]
# 该函数需要三个参数：
# 起始，结束，步长

# 通过range可以创建一个执行指定次数的for循环
for i in range(10):
    print(i)