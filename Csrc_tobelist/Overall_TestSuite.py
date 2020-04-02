#coding:utf-8

import unittest
from  Csrc_tobelist import New_rename,Overall_risk,Overall_risk1,Overall_risk2,Overall_risk3,Overall_risk4,Overall_risk6,Overall_risk7,Overall_risk8,Overall_risk9,Overall_risk10,Overall_risk11,Overall_risk12,Overall_risk13,Overall_risk14
class Overall_suite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ('-'*20 + '开始测试' + '-'*20 +'\n')
        New_rename.Open().open_url()
    @classmethod
    def tearDownClass(cls):
        print ('-'*20 + '结束测试' + '-'*20 +'\n')
        New_rename.Open().driver.close()

    def setUp(self):
        print ('-'*20 + '开始执行测试用例' + '-'*20 +'\n')

    def tearDown(self):
        print ('-'*20 + '结束执行测试用例' + '-'*20 +'\n')


    def test(self):
        Overall_risk.Overall().risk()

    def test1(self):
        Overall_risk1.Overall_1().risk_1()

    def test2(self):
        Overall_risk2.Overall_2().risk_2()
    def test3(self):
        Overall_risk3.Overall_3().risk_3()
    def test4(self):
        Overall_risk4.Overall_4().risk_4()

    def test5(self):
        pass
    def test6(self):
        Overall_risk6.Overall_6().risk_6()
    def test7(self):
        Overall_risk7.Overall_7().risk_7()

    def test8(self):
        Overall_risk8.Overall_8().risk_8()

    def test9(self):
        Overall_risk9.Overall_9().risk_9()

    def test10(self):
        Overall_risk10.Overall_10().risk_10()

    def test11(self):
        Overall_risk11.Overall_11().risk_11()

    def test12(self):
        Overall_risk12.Overall_12().risk_12()
    def test13(self):
        Overall_risk13.Overall_13().risk_13()
    def test14(self):
        Overall_risk14.Overall_14().risk_14()

if __name__ == '__main__':
    # verbosity=*：指数粗错误情况下的信息--默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)


