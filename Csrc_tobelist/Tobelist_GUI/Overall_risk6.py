#coding:utf-8
from Csrc_tobelist.Tobelist_GUI import New_rename
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Overall_6(object):
    driver1 = New_rename.Open.driver
    action = webdriver.ActionChains(driver1)
    lists = New_rename.Open.lists
    def risk_6(self):
        try:
            WebDriverWait(self.driver1,5,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[39]).click())#返回总体页面
        except:
            self.driver1.find_element_by_xpath(self.lists[39]).click()

        tem = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]').text)#获取所有tab标签位置信息
        tem = str(tem).replace('查看详情','').split('\n')#['0交易对手风险', '1关联交易风险', '2指标风险', '3财务异常', '4智能预警风险', '5法律风险', '6舆情风险', '7披露合规分析', '8结构风险', '']
        if self.lists[50] == tem[8]:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[51]))
            self.driver1.find_element_by_xpath(self.lists[51]).click()
            name6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/span').text)#当前所在模块标题
            try:
                if name6 == '结构风险 ':
                    print('结构风险 旧名称为：%s'%(name6))
                elif name6 == '结构风险':
                    print('结构风险 新名称为：%s'%(name6))

            except:
                print('未定位到结构风险模块...%s' %(name6))


            #self.driver1.refresh()
            #time.sleep(10)
            try:
                WebDriverWait(self.driver1,20,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/i'))
                self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/i')).perform()
            except:
                txt6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/p').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取

            txt6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/p').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
            #print(txt6)
            #txt6 = re.sub(r'This text is displayed if your browser does not support the Canvas HTML element\.\n','',txt6)
            try:
                if txt6 == self.lists[17]:
                    print('结构风险的 旧文案为：%s'%(txt6))
                elif txt6 == self.lists[16]:
                    print('结构风险的 新文案为：%s'%(txt6))
                else:
                    print('结构风险的修改文案不正确：%s'%(txt6))

            except:
                print('结构风险的修改文案不正确：%s'%(txt6))

        else:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[7]/a'))
            self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[7]/a').click()
            name6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/span').text)#当前所在模块标题
            try:
                if name6 == '结构风险 ':
                    print('结构风险 旧名称为：%s'%(name6))
                elif name6 == '结构风险':
                    print('结构风险 新名称为：%s'%(name6))

            except:
                print('未定位到结构风险模块...%s' %(name6))

            try:
                WebDriverWait(self.driver1,20,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/i'))
                self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/i')).perform()
            except:
                txt6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/p').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取

            WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/p'))#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
            txt6 = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/p').text
            #print(txt6)
            #txt6 = re.sub(r'This text is displayed if your browser does not support the Canvas HTML element\.\n','',txt6)
            try:
                if txt6 == self.lists[17]:
                    print('结构风险的 旧文案为：%s'%(txt6))
                elif txt6 == self.lists[16]:
                    print('结构风险的 新文案为：%s'%(txt6))
                else:
                    print('结构风险的修改文案不正确：%s'%(txt6))

            except:
                print('结构风险的修改文案不正确：%s'%(txt6))
        return [txt6]
if __name__ == '__main__':
    Overall_6().risk_6()