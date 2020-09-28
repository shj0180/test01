# 单例模式 singleton

class danli:
    __instance =None
    # new 方法本质是构造方法，向内存申请空间，在init前执行
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    # 初始化方法
    def __init__(self,name):
        self.name = name

obj1 = danli('孙悟空')
obj2 = danli('唐僧')

print(obj1.name,obj2.name)

# 反射
class student:
    def __init__(self,name,age,gender):
        self.name =name
        self.age =age
        self.gender = gender


stu = student('孙悟空',600,'M')
# 查询属性名对应的value
val = getattr(stu,'name')
print(val)
# 是否有这个属性
print(hasattr(stu,'name'))



