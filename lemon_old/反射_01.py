
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def dosome(self):
        print('市东南方看来是')

a = Person('tom',18)
b = Person('marry',19)

res = getattr(a,'name')
print(res)

res2 = getattr(a, 'age')

dsf = getattr(a,'dosome')
dsf()