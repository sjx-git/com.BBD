#coding:utf-8
from Csrc_tobelist.Tobelist_GUI import New_rename
from selenium.webdriver.support.wait import WebDriverWait


class Overall_8(object):
    driver1 = New_rename.Open.driver
    lists = New_rename.Open.lists

    def risk_8(self):
        try:
            WebDriverWait(self.driver1,5,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[39]).click())#返回总体页面
        except:
            self.driver1.find_element_by_xpath(self.lists[39]).click()
        name8 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]').text)#当前所在模块标题
        name8 = str(name8).replace('查看详情','')
        #print(name8)
        #print(list(name8))

        try:
            if name8 == self.lists[21]:
                print('总体风险 为旧顺序：%s'%(name8))
            elif name8 == self.lists[20]:
                print('总体风险 为新顺序：%s'%(name8))
            else:
                print('总体风险的排列顺序不正确： %s ' %(name8))
                #print(list(name8))

        except:
            print('总体风险的排列顺序不正确： %s ' %(name8))

        return [name8]
        # print(name8)
        # return name8
if __name__ == '__main__':
    Overall_8().risk_8()
