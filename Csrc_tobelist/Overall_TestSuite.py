#coding:utf8

import unittest
from Csrc_tobelist import Overall_TestCase

class Test_Suite(unittest.TestSuite):
    def test_suite(self):
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Overall_TestCase.Overall_suite))
        return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(Test_Suite().test_suite())