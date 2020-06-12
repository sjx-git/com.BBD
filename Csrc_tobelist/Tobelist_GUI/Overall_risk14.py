#coding:utf-8
from Csrc_tobelist.Tobelist_GUI import New_rename
from selenium.webdriver.support.wait import WebDriverWait


class Overall_14(object):
    driver1 = New_rename.Open.driver
    lists = New_rename.Open.lists

    def risk_14(self):

        #WebDriverWait(self.driver1,50,2).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())#返回总体页面
        self.driver1.find_element_by_xpath(self.lists[39]).click()
        try:
            name14 = WebDriverWait(self.driver1,10,4).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[4]/div/div/div[2]/div/div/div/div/div[1]/table/thead/tr').text)#获取标题列表
        except:
            name14 = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[5]/div[4]/div/div/div[2]/div/div/div/div/div[1]/table/thead/tr').text
        name14 = str(name14).replace('序号\n'
                                     '拟上市公司名称\n'
                                     '拟上市板块\n'
                                     '总体风险程度\n','')
        # print(name14)
        # print(list(name14))

        try:

            if name14 == self.lists[35]:
                print('总体风险--风险排名标题 未调整:%s'%(name14))

            elif name14 == self.lists[34]:
                print('总体风险--风险排名标题 已调整:%s'%(name14))
            else:
                print('总体风险--风险排名标题 调整错了:%s'%(name14))
        except:
            print('总体风险--风险排名标题 调整错了:%s'%(name14))
            # print(list(name14))
            # print(list(self.lists[33]))

        return [name14]
if __name__ == '__main__':
    Overall_14().risk_14()