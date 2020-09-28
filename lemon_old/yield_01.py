# 迭代器是由可迭代对象如list之类调用了iter方法得到的，迭代器调用next就得到值
# 生成器是由yield字段，运行有yield字段的方法就得到生成器，生成器就是自定义迭代器。该生成器调next得到值



def func():
    yield 1
    yield 2



r = func()
print(r)
print(r.__next__())
# print(r.__next__())
print(next(r))




