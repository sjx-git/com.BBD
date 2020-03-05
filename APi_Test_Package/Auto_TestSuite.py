#coding:utf-8
'''
耗费了一天的时间，纵欲解决了在命令行下，iimport包找不到的问题 fuck100遍
1.试了很多sys.path.add啥玩意的 根本不好使  生气
2.还加了一个 乱七八糟的 os 啥的  倒是确实是可以了但是  总觉得别扭
        （import sys
        import os
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = os.path.split(curPath)[0]
        sys.path.append(rootPath)）
3.目前可以接受的方案：在装有requests 的地方可以把HTMLRunner 拿过去，同样可以写个XXX.pth的文件，解决这个恶心的问题
4.内容：就是找不到的这个包的 绝对路径，/root/test/com.bbd/APi_Test_Package  这个包的路径不要写，直接写/root/test/com.bbd 就可以了！！！！！
'''
import unittest
from APi_Test_Package import Request_get,Request_post
import APi_Test_Package.Auto_TestUnitest
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
    def suite_demo(self):#非test开头方法，可以正常被实例化后的类，直接地xx()调用
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
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(APi_Test_Package.Auto_TestUnitest.Auto_test))
        return suite
if __name__ == '__main__':
    '''
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(APi_Test_Package.Auto_TestUnitest.Auto_test))
    unittest.TextTestRunner(verbosity=2).run(suite)
    '''
