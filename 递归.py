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
    if len(s)<2:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return paril(s[1:-1])


print(paril("abcba"))