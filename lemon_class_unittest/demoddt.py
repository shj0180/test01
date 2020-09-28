import unittest_ss
from ddt import ddt,data,unpack
@ddt
class TestDDt(unittest_ss.TestCase):
    @data((1,2),(3,4))
    @unpack
    def test_demo01(self,x,y):
        print(x)
        print(y)
        self.assertEqual(x,1)

    # @data((1, 2), (3, 4))
    # def test_demo02(self, x):
    #     print(x)
    #     self.assertEqual(x, (1,2))

if __name__ == '__main__':
    unittest_ss.main()
