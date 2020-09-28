class A:
    #  实例方法，self 作为参数，需要用对象来调用
    def func(self):  pass

    # 类方法，cls作为参数，用类名调用
    @classmethod
    def func2(cls): pass

    # 静态方法   用类名调用   无默认参数
    @staticmethod
    def fun3(): pass


class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name

one = person('孙悟空',500)
print(one)


















