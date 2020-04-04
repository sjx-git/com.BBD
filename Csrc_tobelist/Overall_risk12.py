#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_12(object):
    driver1 = New_rename.Open.driver
    lists = New_rename.Open.lists

    def risk_12(self):

        #WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[1]/a').click()#进入搜索页面
        try:
            WebDriverWait(self.driver1,10,4).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div[1]/div/div[2]/div').click())#搜产品
        except:
            self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div[1]/div/div[2]/div').click()

        name12 = WebDriverWait(self.driver1,60,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="labelSearchResult"]/div/div[2]/div/div/div/div/div[1]/table/thead/tr/th[4]/div/span[1]/span').text)
        name12 = str(name12).replace('\n是','').rstrip()
        #print(list(name12))

        try:
            if name12 == self.lists[31]:
                print('标题“是否为上市公司” 未被修改:%s'%(name12))
            elif name12 == self.lists[30]:
                print('标题“是否为上市公司” 已被修改:%s'%(name12))
            else:
                print('标题“是否为上市公司” 修改错了:%s'%(name12))
        except:
            print('标题“是否为上市公司” 出错了:%s'%(name12))


if __name__ == '__main__':
    Overall_12().risk_12()