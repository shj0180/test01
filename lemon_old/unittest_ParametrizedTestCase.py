import unittest
# from pylibrary.PyLib import *
from BeautifulReport import BeautifulReport


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param
        print(self.param)

    @staticmethod
    def parametrize(testcase_klass,defName=None, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        if defName != None:
            for name in testnames:
                if name == defName:
                    suite.addTest(testcase_klass(name, param=param))
        else:
            for name in testnames:
                suite.addTest(testcase_klass(name, param=param))
        return suite


class TestOne(ParametrizedTestCase):
    def test_something(self):
        print('param =%s'%self.param)
        print('11')
        self.assertEqual(1, 1)

    def test_something_else(self):
        print(self.param)
        self.assertEqual(2, 2)


# list = [('2018-09-26', '2018-09-26', '测试', '2001', 49, 'TotalCallNum'),
#         ('2018-09-26', '2018-09-26', '测试', '2001', 60, 'TotalCallAnswered'),
#         ('2018-09-26', '2018-09-26', '测试', '2001', 60, 'RingNum'),
#         ('2018-09-13', '2018-09-13', '测试', '2001', 4, 'TotalCallNum_Transfer')]

#
# class Interface_report1(ParametrizedTestCase):
#     def test_Agreport1(self):
#         self.num = self.param[4]
#         self.report_num1 = PyLib().getAgReport(self.param[0],self.param[1],self.param[2],self.param[3])
#         self.report_num=self.report_num1[0][self.param[5]]
#         self.assertEqual(self.num,self.report_num)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestOne,'test_something', param=56))
    suite.addTest(ParametrizedTestCase.parametrize(TestOne, 'test_something_else', param=13))

    unittest.TextTestRunner(verbosity=2).run(suite)














