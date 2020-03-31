#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import time


class Overall_3(object):
    driver1 = New_rename.Open.driver
    lists = New_rename.Open.lists
    def risk_3(self):
        try:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a'))
        except:
            self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click()
        self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[5]/a').click()
        name3 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
        try:
            if name3 == self.lists[9]:
                print('当前的模块 旧名称为：%s'%(name3))
            elif name3 == self.lists[8]:
                print('当前的模块 新名称为：%s'%(name3))
            else:
                print(name3)

        except:
            print('未定位到 %s 模块...' %(name3))

        #time.sleep(10)


if __name__ == '__main__':
    Overall_3().risk_3()