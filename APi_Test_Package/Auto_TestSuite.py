import unittest
from APi_Test_Package import Request_get,Request_post
class Test_Suite(unittest.TestCase):
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
        #此处注意，测试用例必须要先将测试的方法放到 用test方法中，然后通过addTest：类名+（'测试用例的名称'）的方式加入到suite中
        '''第一种添加方法
        test2 = [Test_Suite('test_post'),Test_Suite('test_get')]
        suite.addTests(test2)
        return suite
        '''
        '''第二种添加方法
        suite.addTest(Test_Suite('test_post'))
        suite.addTest(Test_Suite('test_get'))
        return suite
        '''
        '''
        第三种添加方法，貌似这个牛逼 可以自动查找所有测试用例'''
        suite.addTest(unittest.TestLoader.getTestCaseNames(Test_Suite))
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(Test_Suite.suite_demo)