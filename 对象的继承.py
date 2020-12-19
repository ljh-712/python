# 继承
class Animal():
    def run(self):
        print("pao")

    def sleep(self):
        print("shui")


class Dog(Animal):
    def bark(self):
        print("jiao")

d=Dog()
d.run()
print(issubclass(Dog,Animal))