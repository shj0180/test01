import unittest_ss
from lemon_class_unittest.math_method import Math
from ddt import ddt,data
# 测试用例   Testcase
# 执行 TextTestRunner
# 断言
# 报告


@ddt
class TestMathMenth(unittest_ss.TestCase):
    # 测试用例  test_开头
    @data(5,7)
    def test_add_two_positive02(self,x):
        res = Math().add(5,7)
        print(res)
        print(x)
        print('test_add_two_positive')
        # self.assertEqual(3,res)

    def test_add_two_zero02(self):
        res = Math().add(0,0)
        print(res)
        print('test_add_two_zero')
        # self.assertEqual(0,res)

    # @unittest_ss.skip
    def test_add_two_negative02(self):
        res = Math().add(-1,-8)
        print(res)
        print('test_add_two_negative')
        # self.assertEqual(-9, res)


if __name__ == '__main__':
    unittest_ss.main()
































