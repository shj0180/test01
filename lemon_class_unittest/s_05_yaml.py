
import yaml
import unittest_ss
from ddt import file_data,ddt,data

# with open('for01.yml','r',encoding='utf-8') as f:
#     res = yaml.load( f , Loader = yaml.FullLoader)
#     print(res)


@ddt
class YmlTest(unittest_ss.TestCase):

    @file_data('/Users/shihuajun/PycharmProjects/getmouse/for_yaml/for02.yml')
    def test_yml(self,**kwargs):
        print(kwargs.get('name'))
        print(kwargs.get('age'))
        print('**************')




if __name__ == '__main__':
    unittest_ss.main()






