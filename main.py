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

'''web自动化'''
from  Gui_AutoTest import  Sign_in,Ui_demo
if __name__ == '__main__':
    Ui_demo.UiTest.Open_dealmoon('self')
    Sign_in.sign_demo.SignTest('self')