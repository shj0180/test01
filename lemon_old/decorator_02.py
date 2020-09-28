import time
from functools import wraps

def outer(func):
    def inner():
        print("认证成功！")
        result = func()
        print("日志添加成功")
        return result

    return inner


def showtime(func):
    @wraps(func)         # 将func函数的__name__属性等赋值给wrapper函数
    def wrapper(*args,**kwargs):
        t1 = time.time()
        print(t1)
        res = func(*args,**kwargs)

        t2 = time.time()
        print(t2)
        print(t1-t2)
        return res
    return wrapper

@showtime
@outer
def f1():
    print("业务部门1数据接口......")


f1()

