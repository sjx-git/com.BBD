#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_9(object):
    driver1 = New_rename.Open.driver
    lists = New_rename.Open.lists

    def risk_9(self):

        #WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        self.driver1.find_element_by_xpath(self.lists[39]).click()
        WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[4]/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/a'))
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[4]/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/a').click()
        WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/a[1]'))
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/a[1]').click()
        name9 = WebDriverWait(self.driver1,60,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[1]/div[3]/div[1]/div/div/div[5]/div[2]/label').text)

        try:

            if name9 == self.lists[23]:
                print('公司详情--资产评估机构：%s 模块 未被删除'%(name9))
            else:
                print('公司详情--资产评估机构：%s'%(name9))

        except:
            print('公司详情--资产评估机构：%s 模块 已被删除'%(name9))



if __name__ == '__main__':
    Overall_9().risk_9()