import unittest_ss
from ddt import ddt,data,unpack
from BeautifulReport import BeautifulReport

list = [[1, 2, 3, 4], [5, 6, 7, 9]]
list2 =  [['c', 'd', 'c1', 'd1'], ['a', 'b', 'a1', 'b1']]

@ddt
class Demo(unittest_ss.TestCase):

    # @data(*list)
    # @unpack
    # def test_r(self,p1,p2,p3,p4):
    #     print(p1,p2,p3,p4)
    #     self.assertEqual(p1+2,p3)
    #     self.assertEqual(p2+2,p4)

    @data(*list2)
    @unpack
    def test_r2(self,p1,p2,p3,p4):
        print(p1, p2, p3, p4)

if __name__ == '__main__':
    unittest_ss.main()


