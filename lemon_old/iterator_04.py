

di = {('a','b'):[1,2,3],
      ('c','d'):[4,5,6],
      ('e','f'):[7,8,9]
      }

# print(next(enumerate(di, 1)))
# print(next(enumerate(di, 2)))

it = iter(di)
print(next(it))
print(next(it))
for i in di:
    print(i)
