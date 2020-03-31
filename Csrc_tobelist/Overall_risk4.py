#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import time

class Overall_4(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action
    lists = New_rename.Open.lists
    def risk_4(self):
        try:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        except:
            self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[7]/a').click()
        name4 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
        try:
            if name4 == self.lists[11]:
                print('当前的模块 旧名称为：%s'%(name4))
            elif name4 == self.lists[10]:
                print('当前的模块 新名称为：%s'%(name4))

        except:
            print('未定位到 %s 模块...' %(name4))
        #time.sleep(10)#仅做调试中暂停使用，不可用在程序中
        self.action.move_to_element(WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i'))).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
        txt4 = WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        print(list(txt4))
        print(len(txt4))
        try:
            if txt4 == self.lists[13]:
                print('负面舆情监测的 旧文案为：%s'%(txt4))
            elif txt4 == self.lists[12]:
                print('负面舆情监测的 新文案为：%s'%(txt4))
            else:
                print('负面舆情监测的修改文案不正确：%s'%(txt4))

        except:
            print('负面舆情监测的修改文案不正确：%s'%(txt4))

        #time.sleep(10)


if __name__ == '__main__':
    Overall_4().risk_4()