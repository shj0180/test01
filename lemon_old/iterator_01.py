
# with open('iterator.csv','w',encoding='utf-8') as f:
#     f.write('dfsdfdsf\nfsadfdsfsdaf\nfadshdfhsfsdf\ndfhdfshfdhfwefe3043')



with open('iterator.csv','r',encoding='utf-8') as f:
    # fi = f.__iter__()
    # while 1 :
    #     try:
    #         print(fi.__next__().strip('\n')+'@@@@@@')
    #     except StopIteration:
    #         break
    print(f.__next__())
    print(f.__next__())
    # for i in f:
    #     print(i.strip('\n')+'$$%%')

