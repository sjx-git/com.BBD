from  Gui_AutoTest import Sign_in,Ui_demo,My_Home
import unittest
class Case_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('准备')

    @classmethod
    def tearDownClass(cls):
        Ui_demo.UiTest.driver.close()
        print('结束')

    def setUp(self):
        print('开始执行用例')

    def tearDown(self):
        print('执行测试用例结束')

    def test_1(self):
        Ui_demo.UiTest().Open_dealmoon()

    def test_2(self):
        Sign_in.sign_demo().SignTest()

    def test_3(self):
        My_Home.my_demo().my_test()


if __name__ == '__main__':
    Case_test.test_one('self')