#coding:utf-8
from Csrc_tobelist.Tobelist_GUI import New_rename
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Overall_4(object):
    driver1 = New_rename.Open.driver
    action = webdriver.ActionChains(driver1)
    lists = New_rename.Open.lists
    def risk_4(self):
        try:
            WebDriverWait(self.driver1,5,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[39]).click())#返回总体页面
        except:
            self.driver1.find_element_by_xpath(self.lists[39]).click()

        tem = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]').text)#获取所有tab标签位置信息
        tem = str(tem).replace('查看详情','').split('\n')#['0交易对手风险', '1关联交易风险', '2指标风险', '3财务异常', '4智能预警风险', '5法律风险', '6舆情风险', '7披露合规分析', '8结构风险', '']
        if self.lists[46] == tem[6]:
            self.driver1.find_element_by_xpath(self.lists[47]).click()
            name4 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
            try:
                if name4 == self.lists[11]:
                    print('负面舆情监测的 旧名称为：%s'%(name4))
                elif name4 == self.lists[10]:
                    print('负面舆情监测的 新名称为：%s'%(name4))

            except:
                print('负面舆情监测的模块  未定位到 %s ..' %(name4))
            self.action.move_to_element(WebDriverWait(self.driver1,20,2).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i')))#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
            self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i')).perform()
            txt4 = WebDriverWait(self.driver1,20,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
            # print(list(txt4))
            # print(len(txt4))
            try:
                if txt4 == self.lists[13]:
                    print('负面舆情监测的 旧文案为：%s'%(txt4))
                elif txt4 == self.lists[12]:
                    print('负面舆情监测的 新文案为：%s'%(txt4))
                else:
                    print('负面舆情监测的修改文案不正确：%s'%(txt4))

            except:
                print('负面舆情监测的修改文案不正确：%s'%(txt4))
        else:
            self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[5]/a').click()
            name4 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
            try:
                if name4 == self.lists[11]:
                    print('负面舆情监测的 旧名称为：%s'%(name4))
                elif name4 == self.lists[10]:
                    print('负面舆情监测的 新名称为：%s'%(name4))

            except:
                print('负面舆情监测的模块  未定位到 %s ..' %(name4))
            self.action.move_to_element(WebDriverWait(self.driver1,20,2).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i')))#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
            self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i')).perform()
            txt4 = WebDriverWait(self.driver1,20,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
            # print(list(txt4))
            # print(len(txt4))
            try:
                if txt4 == self.lists[13]:
                    print('负面舆情监测的 旧文案为：%s'%(txt4))
                elif txt4 == self.lists[12]:
                    print('负面舆情监测的 新文案为：%s'%(txt4))
                else:
                    print('负面舆情监测的修改文案不正确：%s'%(txt4))

            except:
                print('负面舆情监测的修改文案不正确：%s'%(txt4))

        return [txt4]
if __name__ == '__main__':
    Overall_4().risk_4()