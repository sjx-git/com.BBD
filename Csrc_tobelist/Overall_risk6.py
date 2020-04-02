#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_6(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action
    lists = New_rename.Open.lists
    def risk_6(self):
        WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a'))#返回总体页面
        self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[9]/a').click()
        name6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/span').text)#当前所在模块标题
        try:
            if name6 == '结构风险 ':
                print('当前的模块 旧名称为：%s'%(name6))
            elif name6 == '结构风险':
                print('当前的模块 新名称为：%s'%('结构风险'))

        except:
            print('未定位到 %s 模块...' %(name6))
        #time.sleep(10)#仅做调试中暂停使用，不可用在程序中
        self.action.move_to_element(WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div/i'))).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
        txt6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        txt6 = re.sub(r'This text is displayed if your browser does not support the Canvas HTML element\.\n','',txt6)
        try:
            if txt6 == self.lists[17]:
                print('结构风险的 旧文案为：%s'%(txt6))
            elif txt6 == self.lists[16]:
                print('结构风险的 新文案为：%s'%(txt6))
            else:
                print('结构风险的修改文案不正确：%s'%(txt6))

        except:
            print('结构风险的修改文案不正确：%s'%(txt6))

        #time.sleep(10)


if __name__ == '__main__':
    Overall_6().risk_6()