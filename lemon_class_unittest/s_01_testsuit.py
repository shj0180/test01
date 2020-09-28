import unittest_ss
import HTMLTestRunner
from lemon_class_unittest.s_02_unittest import *

su = unittest_ss.TestSuite()
# loader = unittest_ss.TestLoader()
# su.addTest(loader.loadTestsFromTestCase(TestMathMenth))
# print(loader.loadTestsFromTestCase(TestMathMenth))
# file = open('uninttest.txt','w+')
# runner = unittest_ss.TextTestRunner(stream=file,verbosity=2)
# runner.run(su)

su.addTest(TestMathMenth('test_add_two_positive'))
runner = unittest_ss.TextTestRunner
runner.run(test=TestMathMenth('test_add_two_positive'))


#
# file1 = open('uninttest.html','wb+')
# runner = HTMLTestRunner(stream=file1,verbosity=2)
# runner.run(su)
