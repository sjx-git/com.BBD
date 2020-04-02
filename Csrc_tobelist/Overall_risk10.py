#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_10(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action
    lists = New_rename.Open.lists

    def risk_10(self):

        #WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#
        self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click()#返回总体页面

        WebDriverWait(self.driver1,50,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[4]/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/a'))#选择第一个管理人进详情
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[4]/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/a').click()


        WebDriverWait(self.driver1,70,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div/div[2]/div[1]/div/div[1]/div'))#点击交易对手风险详情
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div/div[2]/div[1]/div/div[1]/div').click()

        WebDriverWait(self.driver1,20,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/span'))#供应商分析
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/span').click()

        name10 = WebDriverWait(self.driver1,60,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div/div/table/tbody/tr[2]/td[1]').text)
        name10_1 = WebDriverWait(self.driver1,60,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div/div[2]/div[2]/div/div[2]/div[2]/div[4]/div/div/div/div/div/table/tbody/tr[3]/td[1]').text)


        try:
            if name10 == self.lists[25]:
                print('前五名供应商采购额的名称 未被修改:%s'%(name10))
            elif name10 == self.lists[24]:
                print('前五名供应商采购额的名称 已被修改:%s'%(name10))
            else:
                print('前五名供应商采购额的名称 修改错了:%s'%(name10))
        except:
            print('前五名供应商采购额的名称 出错了:%s'%(name10))

        try:
            if name10_1 == self.lists[25]:
                print('第一大供应商采购额的名称 未被修改:%s'%(name10_1))
            elif name10 == self.lists[24]:
                print('第一大供应商采购额的名称 已被修改:%s'%(name10_1))
            else:
                print('第一大供应商采购额的名称 修改错了:%s'%(name10_1))
        except:
            print('第一大供应商采购额的名称 出错了:%s'%(name10_1))

if __name__ == '__main__':
    Overall_10().risk_10()