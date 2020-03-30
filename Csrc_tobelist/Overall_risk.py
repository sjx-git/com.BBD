#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
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
        self.driver1.implicitly_wait(80)
        #WebDriverWait(self.driver1,300,2)
        re = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/span').text
        print(re)
        self.action.move_to_element('//*[@id="rigthContent"]/div/div/div/div[3]/div/div/i/svg').perform()
        #tem  = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div/i/svg').click()
        #print(tem)
if __name__ == '__main__':
    Overall().risk()