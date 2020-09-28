# coding:utf-8
import unittest_ss
from selenium import webdriver
import time
# ddt 模块还要依赖nose模块
from ddt import ddt,data,unpack,file_data

# 读取文件类型的还要装PyYaml模块
import yaml
import time

def readtxt():
    par =[]
    # file = open('/Users/shihuajun/PycharmProjects/getmouse/params.txt', 'r', encoding='utf-8')
    # for line in file.readlines():
    #     par.append(line.strip('\n').split(','))
    # return par
    # with open('/Users/shihuajun/PycharmProjects/2019/test01/Auto_Test/data/two.csv','r',encoding='utf-8') as f:
    #     for line in f.readlines():
    #         par.append(line.strip('\n').split(','))
    # print('par：%s'%par)
    # time.sleep(3)
    # return par
    with open('/Users/shihuajun/PycharmProjects/getmouse/params.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            par.append(line.strip('\n').split(','))
    print('par：%s'%par)
    print(type(par))
    return par


@ddt
class Dotest(unittest_ss.TestCase):

    @data(*readtxt())
    @unpack
    def test_t01(self, p1):
        # driver = webdriver.Chrome()
        # driver.get('http://www.baidu.com')
        # driver.find_element_by_id('').send_keys('unittest_ss')
        # driver.find_element_by_id('su').click()
        # time.sleep(5)
        print(p1)
        # print(p2)
        # print()
        print('-------**--')


    # @data((99,22),(1,2))
    #     @unpack
    #     def test01(self,p1,p2):
    #         # driver = webdriver.Chrome()
    #         # driver.get('http://www.baidu.com')
    #         # driver.find_element_by_id('').send_keys('unittest_ss')
    #         # driver.find_element_by_id('su').click()
    #         # time.sleep(5)
    #         print(p1)
    #         print(p2)
    #         print('---------')
# 读取文件类型的还要装PyYaml模块
#     @file_data('par02.yml')
#     # @unpack
#     def test03(self,p3):
#         print(p3)
#         # print(p4)
#         print('***********')



if __name__ == '__main__':
    unittest_ss.main()









