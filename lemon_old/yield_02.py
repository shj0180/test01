
def func():
    while 1:
        x = yield None
        print(x)



g= func()
next(g)
# g.send(None)   # 等同于next(g)
g.send('第三方')
# g.send('第三方2')
#
next(g)
next(g)
# next(g)
#
g.send('第三方23')


