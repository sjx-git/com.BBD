#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_7(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action
    lists = New_rename.Open.lists

    def risk_7(self):
        try:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        except:
            name7 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[2]/div/div[2]/div[1]/div[1]/div').text)#当前所在模块标题
        try:
            if name7 == '结构风险':
                print('当前的模块 旧名称为：%s'%(name7))
            elif name7 == '区域统计概览':
                print('当前的模块 新名称为：%s'%('区域统计概览'))

        except:
            print('未定位到 %s 模块...' %(name7))

        txt7 = WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[2]/div/div[2]/div[1]/div[2]/div/ul[1]/li[1]/div[1]').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        txt7 = re.match(r'\w+、\w+',txt7).group()
        #print(txt7)

        try:
            if txt7 == ('利用图分析技术对公司进行穿透分析，触发交叉持股等风险结构越多，风险值越高 。'):
                print('负面舆情监测的 旧文案为：%s'%(txt7))
            elif  txt7 == '主板、中小板':
                print('区域统计概览的 新文案为：%s'%('主板、中小板'))
            else:
                print('区域统计概览的修改文案不正确：%s'%(txt7))

        except:
            print('区域统计概览的修改文案不正确：%s'%(txt7))

        #time.sleep(10)


if __name__ == '__main__':
    Overall_7().risk_7()