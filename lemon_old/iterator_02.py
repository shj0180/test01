# 把list里每个值加1
list1 = [0,1,2,3,4,5,6,7]

def add_01(list):
    for i in list:
        i +=1
    print(list)

def add_02(list):
    for index,i in enumerate(list):
        list[index] += 1
    print(list)

l = list(enumerate(list1))
print(l)

def add_04(list):
    a = map(lambda x:x+1 ,list)
    print(a)
    for i in a:
        print(i)



if __name__ == '__main__':

    add_01(list1)
    add_02(list1)

    add_04(list1)






