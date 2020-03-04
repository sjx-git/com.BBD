
from APi_Test_Package import Request_get,Request_post
import unittest
class Auto_test(unittest.TestCase):
    '''
    unittest case的运行流程：
        写好一个完整的TestCase
        多个TestCase 由TestLoder被加载到TestSuite里面, TestSuite也可以嵌套TestSuite
        由TextTestRunner来执行TestSuite，测试的结果保存在TextTestResult中
        TestFixture指的是环境准备和恢复
        unittest中最核心的部分是：TestFixture、TestCase、TestSuite、TestRunner

    Test Fixture
        用于测试环境的准备和恢复还原, 一般用到下面几个函数。
        setUp()：准备环境，执行每个测试用例的前置条件
        tearDown()：环境还原，执行每个测试用例的后置条件
        setUpClass()：必须使用@classmethod装饰器，所有case执行的前置条件，只运行一次
        tearDownClass()：必须使用@classmethod装饰器，所有case运行完后只运行一次

    Test Case
        参数verbosity可以控制错误报告的详细程度：默认为1。0，表示不输出每一个用例的执行结果；2表示详细的执行报告结果。
        Verbosity=1情况下成功是 .，失败是 F，出错是 E，跳过是 S
        测试的执行跟方法的顺序没有关系, 默认按字母顺序
        每个测试方法均以 test 开头
        Verbosity=2情况下会打印测试的注释

    Test Suite
        一般通过addTest()或者addTests()向suite中添加。case的执行顺序与添加到Suite中的顺序是一致的
        @unittest.skip()装饰器跳过某个case
        （1）skip():无条件跳过
        @unittest.skip("i don't want to run this case. ")
        （2）skipIf(condition,reason):如果condition为true，则 skip
        @unittest.skipIf(condition,reason)
        （3）skipUnless(condition,reason):如果condition为False,则skip
        @unittest.skipUnless(condition,reason)
        TestSuite和TestCase都有如下方法：
            countTestCases()：返回测试用例的数量。
            run(result)：运行套件相关的测试用例，收集测试结果到result对象中并传给result

    Test Loder
        TestLoadder用来加载TestCase到TestSuite中。
        loadTestsFrom*()方法从各个地方寻找testcase，创建实例，然后addTestSuite，再返回一个TestSuite实例
        defaultTestLoader() 与 TestLoader()功能差不多，复用原有实例
        unittest.TestLoader().loadTestsFromTestCase(testCaseClass)
        unittest.TestLoader().loadTestsFromModule(module)
        unittest.TestLoader().loadTestsFromName(name,module=None)
        unittest.TestLoader().loadTestsFromNames(names,module=None)
        unittest.TestLoader().discover()

    Testing Report:https://www.jianshu.com/p/74654edb5011
        终端报告： 如上terminal 分支
        TXT报告： 如上txt 分支，当前目录会生成ut_log.txt文件
        HTML 报告：如上html 分支，终端上打印运行信息同时会在当前目录生成report文件夹， 文件夹下有test.html和test.log文件
    '''

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
if __name__ == '__main__':
    # verbosity=*：指数粗错误情况下的信息--默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
