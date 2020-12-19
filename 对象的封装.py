#封装：隐藏对象中一些不希望被外部访问到的对象和方法

#为对象的属性添加双下划线开头，表示为隐藏属性，只能在类的内部访问
# __开头的属性隐藏属性，
# 可以为对象的属性使用双下划线开头，__xxx
# 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过对象访问
# 其实隐藏属性只不过是Python自动为属性改了一个名字
#   实际上是将名字修改为了，_类名__属性名 比如 __name -> _Person__name
# class Person:
#     def __init__(self,name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self , name):
#         self.__name = name

# p = Person('孙悟空')

# print(p.__name) __开头的属性是隐藏属性，无法通过对象访问
# p.__name = '猪八戒'
# print(p._Person__name)
# p._Person__name = '猪八戒'

# print(p.get_name())

# 使用__开头的属性，实际上依然可以在外部访问，所以这种方式我们一般不用
#   一般我们会将一些私有属性（不希望被外部访问的属性）以_开头
#   一般情况下，使用_开头的属性都是私有属性，没有特殊需要不要修改私有属性
class Person:
    def __init__(self,name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self , name):
        self._name = name

p = Person('孙悟空')

print(p._name)

