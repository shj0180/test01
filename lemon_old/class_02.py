class dog():
    num =0
    def __init__(self):
        # self.name = name
        # self.size = size
        self.num +=1
        print(self)



d1 = dog()
d2 = dog()
d3 = dog()
print(dog.num)
print(d1.num)
print(d2.num)
print(dog.num)

# 用对象修改局部变量，只要用到赋值，相当于在对象空间中新建了一个变量。而不会修改到静态变量。

class cat():
    num=[]
    def __init__(self):
        self.num.append(1)
        print(self)

c1=cat()
print(c1.num)
print(cat.num)

c2=cat()
print(c1.num)
print(c2.num)
print(cat.num)


class mo():
    num =0
    def __init__(self):
        mo.num +=1;

m1 = mo()
print(mo.num)
print(m1.num)
m2 = mo()
print(mo.num)
print(m1.num)
print(m2.num)

print('----------------------')
class fh:
    '''
     类啊
    '''
    lisf=[]
    def __init__(self):
        self.lisf[0] += 1

sdf= fh
print(sdf)
print(sdf.__dict__)
# 操作静态变量的时候，如果是查看，那么用类名或者对象都可以。如果是修改，那么尽量使用类名进行修改。



