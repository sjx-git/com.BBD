#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import time

class Overall_6(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action

    def risk_6(self):
        try:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        except:
            self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[9]/a').click()
        name6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/span').text)#当前所在模块标题
        try:
            if name6 == '结构风险':
                print('当前的模块 旧名称为：%s'%(name6))
            elif name6 == '结构风险':
                print('当前的模块 新名称为：%s'%('结构风险'))

        except:
            print('未定位到 %s 模块...' %(name6))
        #time.sleep(10)#仅做调试中暂停使用，不可用在程序中
        self.action.move_to_element(WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i'))).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
        txt6 = WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取

        try:
            if txt6 == ('利用图分析技术对公司进行穿透分析，触发交叉持股等风险结构越多，风险值越高。'):
                print('负面舆情监测的 旧文案为：%s'%(txt6))
            elif txt6 == '利用图分析技术对公司进行穿透分析，触发交叉持股等风险结构越多，风险值越高。':
                print('负面舆情监测的 新文案为：%s'%('利用图分析技术对公司进行穿透分析，触发交叉持股等风险结构越多，风险值越高。'))
            else:
                print('负面舆情监测的修改文案不正确：%s'%(txt6))

        except:
            print('负面舆情监测的修改文案不正确：%s'%(txt6))

        #time.sleep(10)


if __name__ == '__main__':
    Overall_6().risk_6()