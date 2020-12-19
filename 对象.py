# 对象：内存中存储数据的一块区域，存放各种数据
# 由三部分组成： id,type,value

# 面向对象：python是面向对象的语言
# 简单理解所有的操作都是通过对象进行的

# 定义类：
# class 类名（[父类] ）

class MyClass():
    pass


print(MyClass)

# 使用类创建一个对象：
mc = MyClass()
print(mc, type(mc))

# isinstance()检擦一个对象是否是一个类的实例
print(isinstance(mc, MyClass))  # True


class Person:
    name = ''
    age = 18

    def say_hello(self):
        print(self.age)
p1=Person()
p1.say_hello()

class Cat:
    def __init__(self):
        print('init方法执行')

    def miao(self):
        print("miao")
c=Cat()



