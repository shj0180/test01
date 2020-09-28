import ddt
import unittest_ss

test_dict = [{"account": "zs", "pwd": "123456"}, {"account": "test", "pwd": "86556"}]
test_list = ['str1', 'str2', 'str3']
test_tuple = [(1, 2), (0, 3), (4, 5)]
list1 = [('a','b'),('c','d')]
list2 = [('a1','b1'),('c1','d1'),('a','b')]

@ddt.ddt
class Test(unittest_ss.TestCase):
    # @ddt.data(*test_dict)
    #     # def test_dict(self, dict):
    #     #     print(dict.get('account', None), dict.get('pwd', None))
    #     #
    #     # @ddt.data(*test_list)
    #     # def test_list(self, test_list):
    #     #     print(test_list)
    #     #
    # @ddt.unpack
    # @ddt.data(*test_tuple)
    # def test_tuple(self, tuple0, tuple1):
    #     print(tuple0, tuple1)

    @ddt.data(*list1)
    @ddt.unpack
    def test_res01(self, p1, p2):
        # print('p1:%s'%p1)
        print(p1)
        print('-'*20)
        print(p2)


if __name__ == "__main__":
    unittest_ss.main(verbosity=2)






