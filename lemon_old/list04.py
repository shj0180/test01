list1 = [1,2,3,6]

list2 = [1,2,3,(3,4),6]
dd = [i for i in list2 if i not in list1]
print(dd)

print(dd[0][1])


list4 = [[''] * 3 for i in range(4)]
print(list4)



