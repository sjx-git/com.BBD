#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re

class Overall_13(object):
    driver1 = New_rename.Open.driver
    lists = New_rename.Open.lists

    def risk_13(self):

        #WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[1]/a').click()#进入搜索页面
        try:
            WebDriverWait(self.driver1,5,2).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div[1]/div/div[2]/div').click())#搜产品
        except:
            self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div[1]/div/div[2]/div').click()

        try:
            name13 = WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="labelSearchResult"]/div/div[2]/div/div/div/div/div[1]/table/thead/tr/th[6]/div/span[1]/span').text)
            name13 = str(name13).replace('\n','').rstrip()
            # print(list(name13))

            if name13 == self.lists[33]:
                print('标题“大数据分类” 未被删除:%s'%(name13))

            else:
                print('标题“大数据分类” 修改错了:%s'%(name13))
            return [name13]
        except:
            print('标题“大数据分类” 已被删除')
            # print(list(name13))
            # print(list(self.lists[33]))

            return None
if __name__ == '__main__':
    Overall_13().risk_13()