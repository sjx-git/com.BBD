import  unittest
from Gui_AutoTest import  Sign_in,Ui_demo,Case_demo
from HTMLTestRunner import HTMLTestRunner
class Suite_demo(unittest.TestCase):

    def suite_case(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Case_demo.Case_test))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(Suite_demo().suite_case())