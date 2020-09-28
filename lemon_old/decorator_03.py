# 有参装饰器
from functools import wraps
import time

def deco(x,y,z):
    def outter(func):
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
    return outter








