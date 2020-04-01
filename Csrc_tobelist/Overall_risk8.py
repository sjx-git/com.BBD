#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_8(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action
    lists = New_rename.Open.lists

    def risk_8(self):
        try:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        except:
            name8 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]').text)#当前所在模块标题
            name8 = str(name8).replace('查看详情','')
        #print(name8)
        #print(list(name8))

        try:
            if name8 == self.lists[21]:
                print('当前的模块 为旧顺序：%s'%(name8))
            elif name8 == self.lists[20]:
                print('当前的模块 为新顺序：%s'%(name8))
            else:
                print('当前模块的排列顺序不正确： %s ' %(name8))
                #print(list(name8))

        except:
            print('当前模块的排列顺序不正确： %s ' %(name8))


if __name__ == '__main__':
    Overall_8().risk_8()
