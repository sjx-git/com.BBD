#coding:utf-8
from Csrc_tobelist import New_rename
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Overall_2(object):
    driver1 = New_rename.Open.driver
    action = webdriver.ActionChains(driver1)
    lists = New_rename.Open.lists
    def risk_2(self):
        try:
            WebDriverWait(self.driver1,5,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[39]).click())
        except:
            self.driver1.find_element_by_xpath(self.lists[39]).click()
        self.driver1.find_element_by_xpath(self.lists[43]).click()
        name2 = WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
        try:
            if name2 == self.lists[5]:
                print('风险指标体系的 旧名称为：%s'%(name2))
            elif name2 == self.lists[4]:
                print('风险指标体系的 新名称为：%s'%(name2))
            else:
                print('风险指标体系的错误%s'%(name2))
        except:
            print('未定位到风险指标体系模块...%s' %(name2))

        WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]'))
        self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]')).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
        WebDriverWait(self.driver1,50,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div'))
        txt2 = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        #print(list(txt2))
        #print(type(tx))
        try:
            if txt2 == self.lists[7]:
                print('风险指标体系的 旧文案为：%s'%(txt2))
            elif txt2 == self.lists[6]:
                print('风险指标体系的 新文案为：%s'%(txt2))
            else:
                print('风险指标体系的修改文案不正确：%s'%(txt2))

        except:
            print('风险指标体系的修改文案不正确：%s'%(txt2))

        return [txt2]

if __name__ == '__main__':
    Overall_2().risk_2()