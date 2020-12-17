# 函数
# 函数也是一个对象
# 对象是内存中专门用来存储数据的区域
# 创建函数：
#    def 函数名([形参1，形参2，形参3])

def fn():
    print("这是我的第一个函数")


fn()


def sum(a, b):
    return a + b


print(sum(1, 2))


# 不定长参数
# 定义一个函数可以求任意数字和
def sum(*a):
    r = 0
    for i in a:
        r += i
    return r


# 定义函数时在形参前面加一个*,这样形参就会获取到所有实参,带*参数只能有一个
# 将所有实参保存到一个元组中
def fn(*a):
    print(a)


fn(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
print(sum(1, 3, 5))


def fn1(**a):
    print(a)


fn1(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
# 参数的解包
t = (10, 20, 30)


def fn2(a, b, c):
    print(a, b, c)
# 要求序列中参数的个数必须和形参一致

fn2(*t)  # 10 20 30


# help()是python内置函数，查询其他python函数的用法
help(print)
# Help on built-in function print in module builtins:
#
# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#
#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.

# 文档字符串：定义函数时，可以在函数内部编写文档字符串
def test(a,b,c) :
    '''这是一个文档字符串示例
    函数的参数是a,b,c
    '''
help(test)

# 命名空间
# 全局命名空间：保存全局变量
# 函数命名空间保存函数中的变量
# locals()用来获取命名空间
print(type(locals()))