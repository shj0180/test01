list1 =[['a','b'],['c','d']]
list2 =[['dfa1','safb1'],['sfa1','bfdsf1'],['a1','b1'],['c1','d1']]

n = len(list1)
print(n)
List_d = []
for i in range(1,n+1):
    print(list1[-i])
    print(list2[-i])
    list_new = list1[-i]+list2[-i]
    print(list_new)
    List_d.append(list_new)
    print('-'*30)
print(List_d)


import unittest_ss
from ddt import ddt,data,unpack
from BeautifulReport import BeautifulReport

# list = [[1, 2, 3, 4], [5, 6, 7, 9]]
# list2 =  [['c', 'd', 'c1', 'd1'], ['a', 'b', 'a1', 'b1']]

@ddt
class Demo(unittest_ss.TestCase):

    # @data(*list)
    # @unpack
    # def test_r(self,p1,p2,p3,p4):
    #     print(p1,p2,p3,p4)
    #     self.assertEqual(p1+2,p3)
    #     self.assertEqual(p2+2,p4)

    @data(*List_d)
    @unpack
    def test_r2(self,p1,p2,p3,p4):
        print(p1, p2, p3, p4)

if __name__ == '__main__':
    unittest_ss.main()


