import unittest
# from pyLibrary.PyLib import *
# from interface.Interface_report1 import *
from BeautifulReport import BeautifulReport
from unittest_ss.parized import ParametrizedTestCase


# list = [('2018-09-26', '2018-09-26', '测试', '', 49, 'TotalCallNum'),
#         ('2018-09-26', '2018-09-26', '测试', '', 60, 'TotalCallAnswered'),
#         ('2018-09-26', '2018-09-26', '测试', '', 60, 'RingNum'),
#         ('2018-09-13', '2018-09-13', '测试', '', 4, 'TotalCallNum_Transfer')]


class Interface_report1(ParametrizedTestCase):
    def test_Agreport1(self):
        self.num = self.param
        print(self.num)



# 用例存放位置
# test_case_path="/Users/shihuajun/PycharmProjects/2019/test01/Auto_Test/Test_Case"
# 测试报告存放位置
log_path='/Users/shihuajun/PycharmProjects/2019/test01/unittest_ss/'
# 测试报告名称
filename='测试报告-百度2'
#用例名称
description='百度登录'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
# pattern="Test_*.py"


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(Interface_report1, 'test_Agreport1', param=123))
    result = BeautifulReport(suite)
    result.report(filename=filename, description=description, log_path=log_path)










