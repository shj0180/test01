import unittest
import ddt

# 测试数据
datas = [ {"user": "admin", "psw": "123", "result": "true"},
        {"user": "admin1", "psw": "1234", "result": "true"},
        {"user": "admin2", "psw": "1234", "result": "true"},
        {"user": "admin3", "psw": "1234", "result": "true"},
        {"user": "admin4", "psw": "1234", "result": "true"},
        {"user": "admin5", "psw": "1234", "result": "true"},
        {"user": "admin6", "psw": "1234", "result": "true"},
        {"user": "admin7", "psw": "1234", "result": "true"},
        {"user": "admin8", "psw": "1234", "result": "true"},
        {"user": "admin9", "psw": "1234", "result": "true"},
        {"user": "admin10", "psw": "1234", "result": "true"},
        {"user": "admin11", "psw": "1234", "result": "true"}]



@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*datas)
    def test01_(self, d):
        """上海-悠悠：{0}"""
        print("测试数据：%s" % d)

    def test02(self):
        print('test02')

    def test03(self):
        print('test03')

if __name__ == "__main__":
    # unittest_ss.main()localtime2
    suit = unittest.TestSuite()
    suit.addTest(Test('test01'))
    # suit.addTest(Test('test02',param=))

    runner = unittest.TextTestRunner()
    runner.run(suit)
