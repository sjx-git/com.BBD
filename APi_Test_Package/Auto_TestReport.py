'''
下载地址：http://tungwaiyip.info/software/HTMLTestRunner.html 。原版的只支持Python 2.x版本，
Python 3.x版本需要做适配。
适配后的下载地址：https://github.com/Slience007/pyunitest/blob/master/untils/HTMLTestRunner.py
安装HTMLTestRunner.py
安装方法
    比较简单，将HTMLTestRunner.py放到python 安装路径的lib下即可。
ubuntu下，我放到了如下路径：/usr/lib/python3.7。
'''

import HTMLTestRunner
import unittest
from APi_Test_Package import Request_get,Request_post
class Test_one(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ('-'*20 + '开始测试' + '-'*20 +'\n')

    @classmethod
    def tearDownClass(cls):
        print ('-'*20 + '结束测试' + '-'*20 +'\n')

    def setUp(self):
        print ('-'*20 + '开始执行测试用例' + '-'*20 +'\n')

    def tearDown(self):
        print ('-'*20 + '结束执行测试用例' + '-'*20 +'\n')
    def test_get(self):
        Request_get.Api_test().test_get()

    def test_post(self):
        Request_post.Api_test1().test_post('1')
    def suite_demo(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.TestLoader.getTestCaseNames(Test_one))
if __name__ == '__main__':
    with open("./TestReport.html","wb") as f:
         runner = HTMLTestRunner(stream = f,title = '测试报告',description= '测试情况',verbosity =2)
         #runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
         runner.run(Test_one.suite_demo)

