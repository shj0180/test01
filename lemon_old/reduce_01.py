from functools import reduce

# reduce 将list内的值做累加，可以设定初始值10，先10+3赋给x，然后再13+4赋给x，这样循环
res = reduce(lambda x,y: x+y, [3,4,5],10)
print(res)

