
# 迭代器是用来迭代取值的工具#
# 有索引的数据类型： 列表，字符串，等
# 为了解决索引迭代器取值的局限性，就有一种不依赖索引的取值方式，就是迭代器
# __iter__() 有此方法说明是可迭代对象



d = {'a':1,'b':2 }
res = d.__iter__()
print(res)               # 返回迭代器





# print(res.__next__())
# print(res.__next__())
# print(res.__next__())       # 异常 StopIteration

# 一个迭代器的值只能取一遍，取干净后再取就取不到了 ，除非再构造一个迭代器
while 1:
    try:
        print(res.__next__())
    except StopIteration:
        break

while 1:
    try:
        print(res.__next__())
    except StopIteration:
        break

# 迭代器是一种更加普遍适用的取值，而如list等适用的是通过索引取值

# ——————————————————————————————
# 上面的写法比较麻烦，比较简单的就是for循环

# 可迭代对象 --- 可以转换成迭代器的对象，就是内置有__iter__方面，
# 调用迭代器对象.__next__()： 得到迭代器的下一个值

# 以上都是通过调用__iter__()来生成迭代器，那样可迭代对象是固定的。
# 自定义迭代器 --- 生成器 yield

list = [23,45]
print(next(iter(list)))



















