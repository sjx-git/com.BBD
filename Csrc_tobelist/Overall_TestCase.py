#coding:utf-8

import unittest
from  Csrc_tobelist import New_rename,Overall_risk,Overall_risk1,Overall_risk2,Overall_risk3,Overall_risk4,Overall_risk5,Overall_risk6,Overall_risk7,Overall_risk8,Overall_risk9,Overall_risk10,Overall_risk11,Overall_risk12,Overall_risk13,Overall_risk14,All_list
class Overall_suite(unittest.TestCase):
    lists = All_list.All_list().lists()
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
        globals()

    def test(self):
        #print(Overall_risk.Overall().risk())
        tem = Overall_risk.Overall().risk()
        #print(tem)
        unittest.TestCase.assertEqual(self,tem[0],self.lists[0])
    def test01(self):
        tem = Overall_risk1.Overall_1().risk_1()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[2])
    def test02(self):
        tem = Overall_risk2.Overall_2().risk_2()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[6])
    def test03(self):
        tem = Overall_risk3.Overall_3().risk_3()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[8])
    def test04(self):
        tem = Overall_risk4.Overall_4().risk_4()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[12])
    def test05(self):
        tem = Overall_risk5.Overall_5().risk_5()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[14])
    def test06(self):
        tem = Overall_risk6.Overall_6().risk_6()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[16])
    def test07(self):
        tem = Overall_risk7.Overall_7().risk_7()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[18])
    def test08(self):
        tem = Overall_risk8.Overall_8().risk_8()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[20])
    def test09(self):
        tem = Overall_risk9.Overall_9().risk_9()
        unittest.TestCase.assertEqual(self,tem[0],None)
    def test10(self):
        tem = Overall_risk10.Overall_10().risk_10()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[24])
    def test11(self):
        tem = Overall_risk11.Overall_11().risk_11()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[28])
    def test12(self):
        tem = Overall_risk12.Overall_12().risk_12()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[30])
    def test13(self):
        tem = Overall_risk13.Overall_13().risk_13()
        unittest.TestCase.assertEqual(self,tem[0],None)
    def test14(self):
        tem = Overall_risk14.Overall_14().risk_14()
        unittest.TestCase.assertEqual(self,tem[0],self.lists[34])

if __name__ == '__main__':
    # verbosity=*：指数粗 错误情况下的信息--默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)


