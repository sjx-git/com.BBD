#coding:utf-8

'''接口自动化
from APi_Test_Package import Request_post, Request_get, Auto_TestReport, Auto_TestSuite, Auto_TestUnitest
import unittest
from HTMLTestRunner import HTMLTestRunner #遇到两次导入只导入了文件名，没导入函数 切记！！！！

if __name__ == '__main__':
    #unittest.main(Auto_TestUnitest)

    suite = unittest.TestSuite()
    #加载用例的时候，一定注意，必须加载的是 加载 类的 类名，不可以直接写到文件名就结束了
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Auto_TestUnitest.Auto_test))
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    unittest.TextTestRunner().run(Auto_TestSuite.Test_Suite().suite_demo())

    with open("TestReport11.html","wb") as f:
        runner = HTMLTestRunner(stream = f,title = u'测试报告',description= u'测试情况',verbosity =2)
        runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
        runner.run(Auto_TestReport.Test_one().suite_demo())
'''

'''web自动化
import unittest
from  Gui_AutoTest import  Sign_in,Ui_demo,Test_Suite
if __name__ == '__main__':

    # Ui_demo.UiTest().Open_dealmoon()
    # Sign_in.sign_demo().SignTest()    
    unittest.TextTestRunner(verbosity=2).run(Test_Suite.Suite_demo().suite_case())
'''
from  Csrc_tobelist import New_rename,Overall_risk,Overall_risk1,Overall_risk2,Overall_risk3,Overall_risk4,Overall_risk6,Overall_risk7,Overall_risk8,Overall_risk9,Overall_risk10,Overall_risk11,Overall_risk12,Overall_risk13
if __name__ == '__main__':
    New_rename.Open().open_url()
    # Overall_risk.Overall().risk()
    # Overall_risk1.Overall_1().risk_1()
    #Overall_risk2.Overall_2().risk_2()
    #Overall_risk3.Overall_3().risk_3()
    #Overall_risk4.Overall_4().risk_4()
    #Overall_risk6.Overall_6().risk_6()
    #Overall_risk7.Overall_7().risk_7()
    #Overall_risk8.Overall_8().risk_8()
    #Overall_risk9.Overall_9().risk_9()
    #Overall_risk10.Overall_10().risk_10()
    #Overall_risk11.Overall_11().risk_11()
    #Overall_risk12.Overall_12().risk_12()
    Overall_risk13.Overall_13().risk_13()




    New_rename.Open().driver.close()

