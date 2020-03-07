from  Gui_AutoTest import Sign_in,Ui_demo
import unittest
class Case_test(unittest.TestCase):

    def test_one(self):
        Ui_demo.UiTest().Open_dealmoon()

    def test_two(self):
        Sign_in.sign_demo().SignTest()

if __name__ == '__main__':
    Case_test.test_one('self')