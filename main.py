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
#from  Csrc_tobelist import New_rename,Overall_risk,Overall_risk1,Overall_risk2,Overall_risk3,Overall_risk4,Overall_risk6,Overall_risk7,Overall_risk8,Overall_risk9,Overall_risk10,Overall_risk11,Overall_risk12,Overall_risk13,Overall_risk14

'''
拟上市
'''
'''
from  Csrc_tobelist import Overall_TestSuite
import unittest,time
from HTMLTestRunner_cn import HTMLTestRunner
if __name__ == '__main__':
    #unittest.TextTestRunner(verbosity=2).run(Overall_TestSuite.Test_Suite().test_suite())
    #自定义包含时间的测试报告
    res = time.strftime('%Y-%m-%d-%H-%M-%S')
    html = 'report'+res+'.html'
    with open(html,"wb") as f:#在文件中用：wb参数 w代表写入，b：是用二进制写入测试报告的内容
        #HTMLTestRunner( stream=open("sample_test_report.html", "wb"), verbosity=2, retry=2, save_last_try=True)
        # 在实例化HTMLTestRunner 对象时追加参数，retry，指定重试次数，如果save_last_try 为True ，一个用例仅显示最后一次测试的结果。如果save_last_try 为False，则显示所有重试的结果。
        runner = HTMLTestRunner(stream = f,title = u'测试报告',description= u'测试情况',verbosity =2)
        #runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'#样式的是否加载 开启就不会加载
        runner.run(Overall_TestSuite.Test_Suite().test_suite())

'''

from Csrs_pe.Csrc_Pe_UI import Open_csrc,Target_risk
if __name__ == '__main__':
    Open_csrc.Open().open_url()
    Target_risk.target_risk().risk()

    Open_csrc.Open().driver.close()




