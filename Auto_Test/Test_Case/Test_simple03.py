import unittest
a = 1
n = 0

def just():
    global n
    if n == 0:
        print('被调用了')
    else:
        pass
    n += 1

class TestMathMenth(unittest.TestCase):
    # 测试用例  test_开头
    def test_add_two_positive01(self):
        print(1)
        just()
        # self.assertEqual(a,2)

    def test_add_two_positive02(self):
        print(2)
        just()

    def test_add_two_positive03(self):
        print(3)
        just()

    def test_add_two_positive00(self):
        print('测试异常')
        try:
            1/0
        except Exception:
            raise Exception('测试异常ok！')


if __name__ == '__main__':
    unittest_ss.main()



















































