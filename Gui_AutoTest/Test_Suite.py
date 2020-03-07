import  unittest
from Gui_AutoTest import  Sign_in,Ui_demo,Case_demo
from HTMLTestRunner import HTMLTestRunner
class Suite_demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('准备')

    @classmethod
    def tearDownClass(cls):
         print('结束')

    def setUp(self):
        print('开始执行用例')

    def tearDown(self):
        print('执行测试用例结束')

    def suite_case(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Case_demo.Case_test))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(Suite_demo().suite_case())