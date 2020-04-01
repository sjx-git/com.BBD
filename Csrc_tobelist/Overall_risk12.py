#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_12(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action
    lists = New_rename.Open.lists

    def risk_12(self):

        #WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[1]/a').click()#进入搜索页面
        try:
            WebDriverWait(self.driver1,1,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div[1]/div/div[2]/div').click())
        #self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div[1]/div/div[2]/div')).double_click()#搜产品
        except:
            self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div[1]/div/div[2]/div').click()

        name12 = WebDriverWait(self.driver1,60,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="labelSearchResult"]/div/div[2]/div/div/div/div/div[1]/table/thead/tr/th[4]/div/span[1]/span').text)

        print(type(name12))
        print(name12)
        print(list(name12))
        '''
        #name11 = self.driver1.find_element_by_id("客户与公司的关联性").text
        name12_1 = WebDriverWait(self.driver1,60,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="供应商与公司的关联性"]/div[1]').text)
        #name11_1 =self.driver1.find_element_by_id("供应商与公司的关联性").text

        try:
            if name12 == self.lists[27]:
                print('标题“客户关联” 未被修改:%s'%(name12))
            elif name12 == self.lists[26]:
                print('标题“客户关联” 已被修改:%s'%(name12))
            else:
                print('标题“客户关联” 修改错了:%s'%(name12))
        except:
            print('标题“客户关联” 出错了:%s'%(name12))

        try:
            if name12_1 == self.lists[29]:
                print('标题“供应商关联” 未被修改:%s'%(name12_1))
            elif name12 == self.lists[28]:
                print('标题“供应商关联” 已被修改:%s'%(name12_1))
            else:
                print('标题“供应商关联” 修改错了:%s'%(name12_1))
        except:
            print('标题“供应商关联” 出错了:%s'%(name12_1))
'          '''
if __name__ == '__main__':
    Overall_12().risk_12()