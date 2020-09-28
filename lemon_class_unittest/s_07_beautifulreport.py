import unittest_ss
from BeautifulReport import BeautifulReport


class UnittestCaseSecond(unittest_ss.TestCase):
    """ 测试代码生成与loader 测试数据"""

    def test_equal(self):
        """
        test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)

    # @BeautifulReport.add_test_img('测试报告.png')
    # def test_is_none(self):
    #     """
    #     test None object
    #     :return:
    #     """
    #     # save_some_img('测试报告.png')
    #     self.assertIsNone(None)

if __name__ == '__main__':
    test_suite = unittest_ss.defaultTestLoader.discover('./', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告3', description='测试deafult报告2', log_path='report')
