from APi_Test_Package import Request_post, Request_get, Auto_TestReport, Auto_TestSuite, Auto_TestUnitest
import unittest

if __name__ == '__main__':

    # unittest.main(Auto_TestUnitest)
    '''
    suite = unittest.TestSuite()
    #记载用例的时候，一定注意，必须加载的是 加载 类的 类名，不可以直接写到文件名就结束了
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Auto_TestUnitest.Auto_test))
    unittest.TextTestRunner(verbosity=2).run(suite)
    '''
    unittest.TextTestRunner().run(Auto_TestSuite.Test_Suite().suite_demo())
    print(Auto_TestSuite.Test_Suite().suite_demo())