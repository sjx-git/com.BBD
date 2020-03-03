import requests
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
    key = '959e4fc1aa5787e67ae143901b2d2673'
    get_url = 'http://apis.juhe.cn/simpleWeather/wids'
    url1 = 'http://apis.juhe.cn/simpleWeather/query'
    city = '1'
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
        par = {"key":self.key}
        ret = requests.get(self.get_url,params = par).json()
        #print( ret)
        if self.assertIn(ret['reason'],'查询成功') == None:##assertIn 判断是否包含在里边 ,true的情况下会返回None 错误会报错
            print('查询成功！')

    def test_post(self):
        #判断city是否为数字或者为汉字  （是否为字母 (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a')）
        if (self.city >= u'\u4e00' and self.city <=u'\u9fa5') or (self.city >= u'\u0030' and self.city<=u'\u0039' ) :
            par = {'key':self.key,'city':self.city}
            rets = requests.post(self.url1,data=par).json()
            #print(rets)
            '''        
            if rets['error_code'] == 207301:
                print('暂不支持该城市')
            else:
                eq = rets['result']['city']
                if self.assertTrue(eq,city) == None:##assertEqual 判断是否一致 ,true的情况下会返回None 错误会报错
                    print('查询成功')
            '''
            try:
                eq = rets['result']['city']
                if self.assertTrue(eq,self.city) == None:##assertEqual 判断是否一致 ,true的情况下会返回None 错误会报错
                    print('查询成功')
            except:
                #print(rets)
                if rets['error_code'] == 207301:
                    print('暂不支持该城市')
                else:
                    print('输入不正确')

if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
    unittest.TestSuite