# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport

# 用例存放位置
test_case_path="/Users/shihuajun/PycharmProjects/2019/test01/Auto_Test/Test_Case"
# 测试报告存放位置
log_path='/Users/shihuajun/PycharmProjects/2019/test01/Auto_Test/Test_Result/Test_Report/'
# 测试报告名称
filename='测试报告-百度2'
#用例名称
description='百度登录'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern="Test_*.py"

class ParametrizedTestCase(unittest.TestCase):  # 可参数化的类
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, defName=None, param=None):  # 参数化方法
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

class Interface_report1(ParametrizedTestCase):
    def test_Agreport1(self):
        self.num = self.param
        print(self.num)



if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(suite)
    result.report(filename=filename,description=description,log_path=log_path)
