#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_11(object):
    driver1 = New_rename.Open.driver
    lists = New_rename.Open.lists

    def risk_11(self):

        #WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        self.driver1.find_element_by_xpath(self.lists[39]).click()#返回总体页面

        WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[4]/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/a'))
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[4]/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/a').click()#风险排名 第一个

        #WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/a[1]'))
        #self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/a[1]').click()# 公司基础详情

        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div/div[2]/div[1]/div/div[2]/div/span').click()# 关联交易风险

        name11 = WebDriverWait(self.driver1,60,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="客户与公司的关联性"]').text)
        #name11 = self.driver1.find_element_by_id("客户与公司的关联性").text
        name11_1 = WebDriverWait(self.driver1,60,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="供应商与公司的关联性"]/div[1]').text)
        #name11_1 =self.driver1.find_element_by_id("供应商与公司的关联性").text

        try:
            if name11 == self.lists[27]:
                print('标题“客户关联” 未被修改:%s'%(name11))
            elif name11 == self.lists[26]:
                print('标题“客户关联” 已被修改:%s'%(name11))
            else:
                print('标题“客户关联” 修改错了:%s'%(name11))
        except:
            print('标题“客户关联” 出错了:%s'%(name11))

        try:
            if name11_1 == self.lists[29]:
                print('标题“供应商关联” 未被修改:%s'%(name11_1))
            elif name11 == self.lists[28]:
                print('标题“供应商关联” 已被修改:%s'%(name11_1))
            else:
                print('标题“供应商关联” 修改错了:%s'%(name11_1))
        except:
            print('标题“供应商关联” 出错了:%s'%(name11_1))
        return [name11_1]
if __name__ == '__main__':
    Overall_11().risk_11()