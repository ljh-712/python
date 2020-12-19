# 求阶乘
def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(5))


# 求幂

def pow(n, i):
    if i == 1:
        return n
    else:
        return n * pow(n, i - 1)


print(pow(2, 3))


# 判断回文
# 先检测第一个字符和最后一个字符是否一致
def paril(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return paril(s[1:-1])


print(paril("abcba"))

# 匿名函数
# 语法：lambda 参数列表：返回值
print(lambda a, b: a + b)  # <function <lambda> at 0x000002298CD7F310>
print((lambda a, b: a + b)(10, 20))
var = lambda i: i % 3 == 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r = filter(lambda i: i % 3 == 0, l)
print(list(r))
l = [1, 2, '3', 5, '4', 4]
# sort() 默认是直接比较列表中元素的大小
l.sort(key=int)  # 将每个数转化为int再排序
print(l)


# sorted()可以对任意序列进行排序
# 使用sorted()函数排序不会影响原来的对象，而是返回一个新对象

# 将函数作为返回值返回，也是一种高阶函数
# 这种高阶函数成为闭包
# 可以将一些私有数据放到闭包
def fn():
    a = 10

    def inner():
        print("我是fn2", a)

    return inner()


fn()
# 求平均值



def make_ave():
    nums = []
    def ave(n):
        nums.append(n)
        return sum(nums) / len(nums)

    return ave


ave = make_ave()
print(ave(10))
print(ave(20))
