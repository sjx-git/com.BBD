#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import time
import re
class Overall(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action

    def risk(self):
        try:
            txt = self.driver1.find_element_by_class_name('activeItem__D3Lq8').text
            print('当前的模块为：%s'%(txt))
        except:
            print('未定位到指定模块...')
        name1  = self.driver1.find_element_by_class_name('secondTopBarTitle__1j4tQ').text
        if  name1 == "风险分类分析":
            print('旧名称为：%s'%(name1))
        elif name1 == '分类风险情况':
            print('新名称为：%s'%('分类风险情况'))
        else:
            print('不正确...')
        self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[1]/a').click()
        #WebDriverWait(self.driver1,300,2)
        # res = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/span').text#当前所在模块标题
        # print(res)
        #time.sleep(3)#仅做调试中暂停使用，不可用在程序中
        WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[1]/i'))
        self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[1]/i')).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
        WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div'))
        tx = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div').text#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        # print(tx)
        # print(type(tx))
        l = re.sub(r'This text is displayed if your browser does not support the Canvas HTML element\.\n','',tx)
        print(l)
        #time.sleep(10)
if __name__ == '__main__':
    Overall().risk()